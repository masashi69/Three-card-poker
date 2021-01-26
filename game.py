import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Three card poker')

GREEN = (0, 127, 0)

width, height = 100, 144
ace1 = pygame.image.load('src/ace_of_spades.png')
ace2 = pygame.image.load('src/ace_of_hearts.png')
ace3 = pygame.image.load('src/ace_of_diamonds.png')
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