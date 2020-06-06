import random

class Deck:

	def __init__(self):
		self.deck = []
		self.build()

	def build(self):
		self.value = [x for x in range(2,15)] # Ace is 14
		self.suit = ['♠', '♡', '♢', '♣']

		for s in self.suit:
			for v in self.value:
				self.deck.append(''.join([s, str(v)]))

		return self

	def show(self):
		for c in self.deck:
			print(c)

	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self):
		return self.deck.pop(0)

class Handcheck:

	def __init__(self, hand, flag=False):
		self.hand = hand
		self.flag = flag

		if self.flag == True:
			self.player = Judge(self.hand, dealer=True)
		else:
			self.player = Judge(self.hand)

	def get_role(self):
		return list(self.player[0].keys()), self.player[1]

	def result(self):
		return list(self.player[0].values()), self.player[1]

class Payoff:

	# Use "in" to hand return as a list

	def __init__(self, bet, hand):
		self.bet = bet
		self.hand = hand

	def anti_bonus(self):
		if 4 in self.hand:
			return self.bet * 1
		elif 5 in self.hand: 
			return self.bet * 4
		elif 6 in self.hand:
			return self.bet * 5
		else:
			return 0

	def pairplus_bonus(self):
		if 2 in self.hand:
			return self.bet * 1
		elif 3 in self.hand:
			return self.bet * 4
		elif 4 in self.hand:
			return self.bet * 6
		elif 5 in self.hand: 
			return self.bet * 30
		elif 6 in self.hand: 
			return self.bet * 40
		else:
			return 0

def Handout(card):
	hand = []
	for i in range(3):
		hand.append(card.draw())

	return hand


def Judge(hands, dealer=False):

	# Devide hands into suits and numbers
	suit = [ hands[0][0] , hands[1][0] , hands[2][0] ]
	rank = [ int(x[1:]) for x in hands ]

	# Sort of numbers for role evaluation
	rank.sort()

	# Evaluation of hand
	if len(set(suit)) == 1 and rank[1] == rank[0] + 1 and rank[2] == rank[1] + 1:
		return {'Straight Flash!': 6}, rank
	elif len(set(suit)) == 1 and rank[0] == 14 and rank[1] == 2 and rank[2] == 1:
		return {'Straight Flash!': 6}, rank
	elif len(set(rank)) == 1:
		return {'Three of a kind!': 5}, rank
	elif rank[1] == rank[0] + 1 and rank[2] == rank[1] + 1:
		return {'Straight!': 4}, rank
	elif rank[0] == 14 and rank[1] == 2 and rank[2] == 1:
		return {'Straight!': 4}, rank
	elif len(set(suit)) == 1:
		return {'Flash!': 3}, rank
	elif len(set(rank)) == 2:
		return {'One Pair!': 2}, rank
	elif max(rank) < 12 and dealer == True:
		return {'Less than Queen-high. Dealer can\'t play': 0}, rank
	elif max(rank):
		return {'High card!': 1}, rank
		

def Match(p1, p2):

	if p1[0] > p2[0]:
		return 0
	elif p1[0] < p2[0]:
		return 1
	# Compare number in case draw rank hand high to low
	elif p1[0] == p2[0]:
		if p1[1][2] > p2[1][2]:
			return 0
		elif p1[1][2] < p2[1][2]:
			return 1
		elif p1[1][2] == p2[1][2]:
			if p1[1][1] > p2[1][1]:
				return 0
			elif p1[1][1] < p2[1][1]:
				return 1
			elif p1[1][1] == p2[1][2]:
				if p1[1][0] > p2[1][0]:
					return 0
				elif p1[1][0] < p2[1][0]:
					return 1
		# Player wins in case of draw
		else:
			return 0

def Shaping(hand):

	h = []
	
	for i in hand:
		if '11' in i:
			h.append(i.replace('11', 'J'))
		elif '12' in i:
			h.append(i.replace('12', 'Q'))
		elif '13' in i:
			h.append(i.replace('13', 'K'))
		elif '14' in i:
			h.append(i.replace('14', 'A'))
		else:
			h.append(i)
	return h

# main
def main(chip):

	print('Your chips are ${}.'.format(chip))

	# Ante
	while True:
		i = input('Do you want to bet ante?: [y/n]')
		if i == 'y':
			ante = input('How much do you bet?: $')
			try:
				ante = int(ante)
				bet_ante = ante

			except:
				pass

			break 

		elif i == 'n':
			bet_ante = 0
			break 

		else:
			pass

	# Pair plus
	while True:
		i = input('Do you want to bet Pair plus?: [y/n]')
		if i == 'y':
			pp = input('How much do you bet?: $')
			try:
				pp = int(pp)
				bet_pairplus =  pp

			except:
				pass

			break

		elif i == 'n':
			bet_pairplus = 0
			break

		else:
			pass

	# Game start
	card = Deck()
	card.shuffle()

	player = Handout(card)
	dealer = Handout(card)

	p_hand = Handcheck(player).result()
	d_hand = Handcheck(dealer, flag=True).result()

	p_role = Handcheck(player).get_role()
	d_role = Handcheck(dealer, flag=True).get_role()

	p_show = Shaping(player)
	d_show = Shaping(dealer)

	print("\n===== Open Your Hand =====\n")
	print("Your Hand: {} {}\n".format( p_show, p_role[0] ))

	# bet, fold

	print('The same chips as Ante is required to match the dealer.')
	while True:

		if bet_ante == 0 and bet_pairplus == 0:
			refund_bet = 0
			refund_ante = 0
			break

		else:

			i = input('Do you play in your hand?: [y/n]')

			# Open dealer hand

			print("\n===== Open Dealer Hand =====\n")
			print("Dealer Hand: {} {}\n".format( d_show, d_role[0] ))

			if i == 'y':
				try:
					# b = int(b)
					bet_play = bet_ante

					# Win / Lose Judge
					
					match = Match(p_hand, d_hand)
					# If the dealer folds, only ante will be refunded
					if match == 0 and d_hand[0][0] == 0:
						print('You WIN!')

						refund_bet = bet_play * 1
						refund_ante = bet_play * 2

					elif match == 0:
						print('You WIN!')

						refund_bet = bet_play * 2
						refund_ante = bet_play * 2

					elif match == 1:
						print('Dealer WIN!')

						# Forfelt the bet and ante
						refund_bet = 0
						refund_ante = 0

						chip = chip - (bet_play + bet_ante + bet_pairplus)

				except:
					pass

			elif i == 'n':
				print('You folded.')

				# bet confiscation
				chip = chip - (bet_ante + bet_pairplus)

				refund_bet = 0
				refund_ante = 0
				bet_ante = 0
				bet_pairplus = 0

			break

	# pay off
	# Win refund
	all_refund = refund_ante + refund_bet

	# Hand bonus
	pay_ante = Payoff(bet_ante, p_hand[0]).anti_bonus()
	pay_pairplus = Payoff(bet_pairplus, p_hand[0]).pairplus_bonus()

	# To reuse the chips for main loop
	global total

	total = chip + (all_refund + pay_ante + pay_pairplus)

	# For shape strings
	payoff_print =  'Pay off ${} \n' \
					'Pair plus bonus ${} \n' \
					'Ante bonus ${}'.format(all_refund, pay_pairplus, pay_ante)

	print('\n===== Pay off =====\n')
	print(payoff_print, '\n')
	print('Your chips are ${}.'.format(total))

if __name__ == '__main__':

	# Initial chips
	chip = 1000

	while True:
		main(chip)
		i = input('Continue?: [y/n]')
		if i == 'y':
			chip = total
		elif i == 'n':
			break
		else:
			pass

