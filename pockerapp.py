
import random


class Deck:

	def __init__(self):
		self.deck = []
		self.build()

	def build(self):
		self.value = [x for x in range(2,15)] # Ace is 14
		self.suit = ['S', 'H', 'D', 'C']

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


def Handout(card):
	hand = []
	for i in range(3):
		hand.append(card.draw())

	return hand


def Judge(hands, dealer=False):

	# Devide hands into suits and numbers
	suit = [ hands[0][0] , hands[1][0] , hands[2][0] ]
	rank = [int(x[1:]) for x in hands]

	# Sort of numbers for role evaluation
	rank.sort()

	# Evaluation of hand
	if len(set(suit)) == 1 and rank[1] == rank[0] + 1 and rank[2] == rank[1] + 1:
		return {'Straight Flash': 6}, max(rank)
	elif len(set(rank)) == 1:
		return {'Three of a kind!': 5}, max(rank)
	elif rank[1] == rank[0] + 1 and rank[2] == rank[1] + 1:
		return {'Straight!': 4}, max(rank)
	elif len(set(suit)) == 1:
		return {'Flash!': 3}, max(rank)
	elif len(set(rank)) == 2:
		return {'One Pair!': 2}, max(rank)
	elif max(rank) < 12 and dealer == True:
		return {'Dealer can\'t play': 0}, max(rank)
	elif max(rank):
		return {'High card!': 1}, max(rank)
		

def Match(p1, p2):

	if p1[0] > p2[0]:
		print('Player WIN!')
	elif p1[0] < p2[0]:
		print('Dealer WIN!')
	# Compare number in case draw rank hand
	elif p1[0] == p2[0]:
		if p1[1] > p2[1]:
			print('Player WIN!')
		elif p1[1] < p2[1]:
			print('Dealer WIN!')
		# Player wins in case of draw
		else:
			print('Player WIN!')

# main
def main():

	# Ante

	# Game start
	card = Deck()
	card.shuffle()

	player = Handout(card)
	dealer = Handout(card)

	p_hand = Handcheck(player).result()
	d_hand = Handcheck(dealer, flag=True).result()

	p_role = Handcheck(player).get_role()
	d_role = Handcheck(dealer, flag=True).get_role()

	print("Player Hand: {} {}\nDealer Hand: {} {}\n".format( \
		player, p_role[0], \
		dealer, d_role[0] ))

	Match(p_hand, d_hand)

	# bet, fold

	# pay off

if __name__ == '__main__':
	main()
