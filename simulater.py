import pokerapp
import collections

match_list = []
hand_list = []
win_list = []

trial = 1000

ante = 10
bet_chip = ante
pp = 10

def Trials(chips):
	games = 0
	for _ in range(trial):
		# Cannot bet more than chips
		if chips >= (ante + pp + bet_chip):
			deck = pokerapp.Deck()
			deck.shuffle()

			player = pokerapp.Handout(deck)
			dealer = pokerapp.Handout(deck)

			hand_result = pokerapp.Handcheck(player).get_role()[0][0]
			player_hand = pokerapp.Handcheck(player).result()
			dealer_hand = pokerapp.Handcheck(dealer, flag=True).result()

			match_result = pokerapp.Match(player_hand, dealer_hand)

			# bonus
			ante_b = pokerapp.Payoff(ante, player_hand[0]).ante_bonus()
			pp_b = pokerapp.Payoff(pp, player_hand[0]).pairplus_bonus()

			if match_result == 0:
				win_list.append(hand_result)
			elif match_result == 2:
				ante_b = 0
				pp_b = 0
		
			match_list.append(match_result)
			hand_list.append(hand_result)

			# Reduce bet chips
			chips = chips - (ante + bet_chip + pp)

			# pay off
			pays = pokerapp.Liquidation(match_result, dealer_hand, ante, bet_chip)

			chips = chips + pays + ante_b + pp_b

			# For debug
			#print(hand_result, match_result, chips, pays, ante_b, pp_b)
			games += 1
		else:
			break

	return chips, games

def Wins(games):
	w = collections.Counter(match_list)
	print('Player {} wins. ({:.1%})'.format(w[0], w[0] / games))
	print('Dealer {} wins. ({:.1%})'.format(w[1], w[1] / games))
	print('Draw {} times. ({:.1%})'.format(w[2], w[2] / games))

	return w[0]

def Hands(lists, times):

	# Sort percntages in descending order
	hand_dict = collections.Counter(lists)
	sorted_hand_dict = sorted(hand_dict.items(), key=lambda x:x[1], reverse=True)

	for hand, prob in sorted_hand_dict:
		# Convert to str to use rjust
		p  = str(round((prob / times) * 100, 3))

		shaped_hand = hand.ljust(16)
		shaped_propotion = (p + '%').rjust(10)

		print(shaped_hand, shaped_propotion)


def Save_details(text):
	with open('details.txt', 'w') as f:
		f.write(text)

def main():

	chip = 1000

	print('You are first given ${:,}.'.format(chip))
	print('Three card poker simulator start.')
	print('The simulator trials {:,} times.'.format(trial))
	print('You\'ll bet ante ${} and pair plus ${} all the time.'.format(ante, pp))

	T, G = Trials(chip)

	print()
	print('You could play the game {:} times.'.format(G))

	print('\n=== Probabliry of winning or losing ===\n')

	W = Wins(G)

	print('\n=== Percentage of Players all hands ===\n')
	
	Hands(hand_list, G)

	print('\n=== Percentage of Players win({:,} times) hands ===\n'.format(W))
	
	Hands(win_list, W)

	print()
	print('You finally got ${:,}'.format(T))

if __name__ == '__main__':
	main()

 
