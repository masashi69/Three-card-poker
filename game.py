import pygame
import sys
from pygame.locals import *
import pokerapp

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Three card poker')

GREEN = (0, 127, 0)

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

ace1 = pygame.image.load(card_images[player_hand[0]])
ace2 = pygame.image.load(card_images[player_hand[1]])
ace3 = pygame.image.load(card_images[player_hand[2]])
card1 = pygame.transform.scale(ace1, (width, height))
card2 = pygame.transform.scale(ace2, (width, height))
card3 = pygame.transform.scale(ace3, (width, height))

while True:

	DISPLAYSURF.fill(GREEN)

	x, y = 10, 10
	DISPLAYSURF.blit(card1, (x,y))
	DISPLAYSURF.blit(card2, (x + width,y))
	DISPLAYSURF.blit(card3, (x + width * 2,y))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()