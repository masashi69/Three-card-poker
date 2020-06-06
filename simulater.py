import pokerapp
import collections

match_list = []
hand_list = []
win_list = []

trial = 1000000

def Trials():
	for _ in range(trial):

	    deck = pokerapp.Deck()
	    deck.shuffle()

	    player = pokerapp.Handout(deck)
	    dealer = pokerapp.Handout(deck)

	    match_result = pokerapp.Match(player, dealer)
	    hand_result = pokerapp.Handcheck(player).get_role()[0][0]

	    if match_result == 0:
		    win_list.append(hand_result)
	    
	    match_list.append(match_result)
	    hand_list.append(hand_result)

def Wins():
	w = collections.Counter(match_list)
	print('Player {} wins.'.format(w[0]))
	print('Dealer {} wins.'.format(w[1]))
	print('Draw {} times.'.format(w[2]))

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

def main():

	print('Three card poker simulator start.')
	print('The simulator trials {:,} times.'.format(trial))

	Trials()

	print('\n=== Probabliry of winning or losing ===\n')

	W = Wins()

	print('\n=== Percentage of Players all hands ===\n')
	
	Hands(hand_list, trial)

	print('\n=== Percentage of Players win({:,} times) hands ===\n'.format(W))
	
	Hands(win_list, W)


if __name__ == '__main__':
	main()

 