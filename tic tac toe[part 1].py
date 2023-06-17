import pygame, sys#, random, time
import numpy as np
pygame.init()

ROWS = 3
COLUMNS = 3
WIDTH = 600
HEIGHT = 600
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

#RGB
GREEN = (50, 100, 0)
RED = (100, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


board = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" TIC TAC TOE ")
board.fill(GREEN)


