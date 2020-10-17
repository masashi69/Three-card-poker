import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Three card poker')

GREEN = (0, 127, 0)

while True:

	DISPLAYSURF.fill(GREEN)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()