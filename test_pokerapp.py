import unittest
import pokerapp

class TestPokerApp(unittest.TestCase):

	def setUp(self):
		self.card = pokerapp.Deck()
		
	def test_createdeck(self):
		self.card.shuffle()

	def test_player(self):
		player = pokerapp.Handout(self.card)

		p_hand = pokerapp.Handcheck(player).result()
		p_role = pokerapp.Handcheck(player).get_role()

		self.assertRegex(str(p_hand), '\(\[\d\], \[(\d*, ){2}\d*\]\)')
		self.assertRegex(str(p_role), '.+\!')

	def test_dealer(self):
		dealer = pokerapp.Handout(self.card)

		d_hand = pokerapp.Handcheck(dealer, flag=True).result()
		d_role = pokerapp.Handcheck(dealer, flag=True).get_role()

		self.assertRegex(str(d_hand), '\(\[\d\], \[(\d*, ){2}\d*\]\)')
		self.assertRegex(str(d_role), '.+\!|.+')

	def test_match(self):
		player = pokerapp.Handout(self.card)
		dealer = pokerapp.Handout(self.card)

		p_hand = pokerapp.Handcheck(player).result()
		d_hand = pokerapp.Handcheck(dealer, flag=True).result()

		match = pokerapp.Match(p_hand, d_hand)
		self.assertEqual(match, 0 or 1 or 2)

	def test_payoff(self):
		player = pokerapp.Handout(self.card)

		p_hand = pokerapp.Handcheck(player).result()

		pay_ante = pokerapp.Payoff(10, p_hand[0]).ante_bonus()
		pay_pairplus = pokerapp.Payoff(10, p_hand[0]).pairplus_bonus()

		self.assertRegex(str(pay_ante), '\d+')
		self.assertRegex(str(pay_pairplus), '\d+')


if __name__ == '__main__':
	unittest.main()	
