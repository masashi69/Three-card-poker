import pygame
import sys
from pygame.locals import *
import pokerapp

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Three card poker')

GREEN = (0, 127, 0)

# Use the hand list as it is as a key
card_images = {'♠2': 'src/2_of_spades.png', '♠3': 'src/3_of_spades.png',
			   '♠4': 'src/4_of_spades.png', '♠5': 'src/5_of_spades.png',
			   '♠6': 'src/6_of_spades.png', '♠7': 'src/7_of_spades.png',
			   '♠8': 'src/8_of_spades.png', '♠9': 'src/9_of_spades.png',
			   '♠10': 'src/10_of_spades.png', '♠11': 'src/jack_of_spades.png',
			   '♠12': 'src/queen_of_spades.png', '♠13': 'src/king_of_spades.png',
			   '♠14': 'src/ace_of_spades.png', '♡2': 'src/2_of_hearts.png',
			   '♡3': 'src/3_of_hearts.png', '♡4': 'src/4_of_hearts.png',
			   '♡5': 'src/5_of_hearts.png', '♡6': 'src/6_of_hearts.png',
			   '♡7': 'src/7_of_hearts.png', '♡8': 'src/8_of_hearts.png',
			   '♡9': 'src/9_of_hearts.png', '♡10': 'src/10_of_hearts.png',
			   '♡11': 'src/jack_of_hearts.png', '♡12': 'src/queen_of_hearts.png',
			   '♡13': 'src/king_of_hearts.png', '♡14': 'src/ace_of_hearts.png',
			   '♢2': 'src/2_of_diamonds.png', '♢3': 'src/3_of_diamonds.png',
			   '♢4': 'src/4_of_diamonds.png', '♢5': 'src/5_of_diamonds.png',
			   '♢6': 'src/6_of_diamonds.png', '♢7': 'src/7_of_diamonds.png',
			   '♢8': 'src/8_of_diamonds.png', '♢9': 'src/9_of_diamonds.png',
			   '♢10': 'src/10_of_diamonds.png', '♢11': 'src/jack_of_diamonds.png',
			   '♢12': 'src/queen_of_diamonds.png', '♢13': 'src/king_of_diamonds.png',
			   '♢14': 'src/ace_of_diamonds.png', '♣2': 'src/2_of_clubs.png',
			   '♣3': 'src/3_of_clubs.png', '♣4': 'src/4_of_clubs.png',
			   '♣5': 'src/5_of_clubs.png', '♣6': 'src/6_of_clubs.png',
			   '♣7': 'src/7_of_clubs.png', '♣8': 'src/8_of_clubs.png',
			   '♣9': 'src/9_of_clubs.png', '♣10': 'src/10_of_clubs.png',
			   '♣11': 'src/jack_of_clubs.png', '♣12': 'src/queen_of_clubs.png',
			   '♣13': 'src/king_of_clubs.png', '♣14': 'src/ace_of_clubs.png'}

width, height = 100, 144

# poker play
deck = pokerapp.Deck()
deck.shuffle()

player_hand = pokerapp.Handout(deck)
dealer_hand = pokerapp.Handout(deck)

p_handcheck = pokerapp.Handcheck(player_hand).result()
d_handcheck = pokerapp.Handcheck(dealer_hand, flag=True).result()

p_role = pokerapp.Handcheck(player_hand).get_role()
d_role = pokerapp.Handcheck(dealer_hand, flag=True).get_role()

def Matchcheck():
	match_result = pokerapp.Match(p_handcheck, d_handcheck)

	if match_result == 0:
		return 'You WIN!'

	elif match_result == 1:
		return 'Dealer WIN!'

	elif match_result == 2:
		return 'Draw!'

winner = Matchcheck()

font = pygame.font.Font(None, 20)
winner_text = font.render(winner, True, (255,255,255))
p_role_text = font.render('Player hand: ' + p_role[0][0], True, (255,255,255))
d_role_text = font.render('Dealer hand: ' + d_role[0][0], True, (255,255,255))

img1 = pygame.image.load(card_images[player_hand[0]])
img2 = pygame.image.load(card_images[player_hand[1]])
img3 = pygame.image.load(card_images[player_hand[2]])
img4 = pygame.image.load(card_images[dealer_hand[0]])
img5 = pygame.image.load(card_images[dealer_hand[1]])
img6 = pygame.image.load(card_images[dealer_hand[2]])

# Resize card image
p_card1 = pygame.transform.scale(img1, (width, height))
p_card2 = pygame.transform.scale(img2, (width, height))
p_card3 = pygame.transform.scale(img3, (width, height))
d_card1 = pygame.transform.scale(img4, (width, height))
d_card2 = pygame.transform.scale(img5, (width, height))
d_card3 = pygame.transform.scale(img6, (width, height))



while True:

	DISPLAYSURF.fill(GREEN)

	x, y = 10, 10
	# Player hand
	DISPLAYSURF.blit(p_card1, (x,y))
	DISPLAYSURF.blit(p_card2, (x + width,y))
	DISPLAYSURF.blit(p_card3, (x + width * 2,y))
	# Dealer hand
	DISPLAYSURF.blit(d_card1, (x,y + height))
	DISPLAYSURF.blit(d_card2, (x + width,y + height))
	DISPLAYSURF.blit(d_card3, (x + width * 2,y + height))

	DISPLAYSURF.blit(p_role_text, (400, 260))
	DISPLAYSURF.blit(d_role_text, (400, 280))
	DISPLAYSURF.blit(winner_text, (400, 300))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()