import pokerapp
import collections

match_list = []
hand_list = []

trial = 500000

def Trials():
	for _ in range(trial):

	    deck = pokerapp.Deck()
	    deck.shuffle()

	    player = pokerapp.Handout(deck)
	    dealer = pokerapp.Handout(deck)

	    match_result = pokerapp.Match(player, dealer)
	    hand_result = pokerapp.Handcheck(player).get_role()[0][0]
	    
	    match_list.append(match_result)
	    hand_list.append(hand_result)

def Wins():
	for w in collections.Counter(match_list).items():
		if w[0] == 0:
			print('Player {} wins.'.format(w[1]))
		else:
			print('Dealer {} wins.'.format(w[1]))

def Hands():

	# Sort percntages in descending order
	hand_dict = collections.Counter(hand_list)
	sorted_hand_dict = sorted(hand_dict.items(), key=lambda x:x[1], reverse=True)

	for hand, prob in sorted_hand_dict:
		# Convert to str to use rjust
		p  = str(round((prob / trial) * 100, 3))

		shaped_hand = hand.ljust(16)
		shaped_propotion = (p + '%').rjust(10)

		print(shaped_hand, shaped_propotion)

def main():

	print('Three card poker simulator start.')
	print('The simulator trials {} times.'.format(trial))

	Trials()

	print('\n=== Probabliry of winning or losing ===\n')

	Wins()

	print('\n=== Percentage of Players hands ===\n')
	
	Hands()

if __name__ == '__main__':
	main()

 