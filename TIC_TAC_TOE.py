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

pygame.draw.line(board, RED, (30, 200), (570, 200), 5)
pygame.draw.line(board, RED, (30, 400), (570, 400), 5)
pygame.draw.line(board, RED, (200, 30), (200, 570), 5)
pygame.draw.line(board, RED, (400, 30), (400, 570), 5)
pygame.draw.line(board, RED, (0, 0), (0, 600), 15)
pygame.draw.line(board, RED, (0, 0), (600, 00), 15)
pygame.draw.line(board, RED, (600, 0), (600, 600), 15)
pygame.draw.line(board, RED, (0, 600), (600, 600), 15)

'''pygame.draw.rect(board, RED, pygame.Rect(30, 30, 140, 140), 5)
pygame.draw.rect(board, RED, pygame.Rect(30, 230, 140, 140), 5)
pygame.draw.rect(board, RED, pygame.Rect(30, 430, 140, 140), 5)
pygame.draw.rect(board, RED, pygame.Rect(230, 30, 140, 140), 5)
pygame.draw.rect(board, RED, pygame.Rect(430, 30, 140, 140), 5)
pygame.draw.rect(board, RED, pygame.Rect(230, 230, 140, 140), 5)
pygame.draw.rect(board, RED, pygame.Rect(430, 430, 140, 140), 5)
pygame.draw.rect(board, RED, pygame.Rect(430, 230, 140, 140), 5)
pygame.draw.rect(board, RED, pygame.Rect(230, 430, 140, 140), 5)'''

board_arr = np.zeros((ROWS, COLUMNS)) #[[0,0,0],[0,0,0],[0,0,0]]


def player_mark(row, col, player):
    board_arr[row][col] = player


def is_block_available(row, col):
    return board_arr[row, col] == 0


def draw_figure(row, col):
            if board_arr[row][col] == 1:
                pygame.draw.circle(board, WHITE, (int(col * 200 + (200 / 2)), int(row * 200 + (200/2))), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board_arr[row][col] == 2:
                pygame.draw.line(board, BLACK, (col * 200 + 55, row * 200 + 200 - 55), (col * 200 + 200 - 55, row * 200 + 55), CROSS_WIDTH)
                pygame.draw.line(board, BLACK, (col * 200 + 55, row * 200 + 55), (col * 200 + 200 - 55, row * 200 + 200 - 55), CROSS_WIDTH)

def check_winner(player):
	# vertical win check
	for col in range(COLUMNS):
		if board_arr[0][col] == player and board_arr[1][col] == player and board_arr[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	# horizontal win check
	for row in range(ROWS):
		if board_arr[row][0] == player and board_arr[row][1] == player and board_arr[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# ascending diagonal win check
	if board_arr[2][0] == player and board_arr[1][1] == player and board_arr[0][2] == player:
		draw_asc_diagonal(player)
		return True

	# descending diagonal win chek
	if board_arr[0][0] == player and board_arr[1][1] == player and board_arr[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False
    
def draw_vertical_winning_line(col, player):
	posX = col * 200 + 200 //2

	if player == 1:
		color = WHITE
	elif player == 2:
		color = BLACK

	pygame.draw.line( screen, color, (posX, 30), (posX, HEIGHT - 30), 15 )

def draw_horizontal_winning_line(row, player):
	posY = row * 200 + 200//2

	if player == 1:
		color = WHITE
	elif player == 2:
		color = BLACK

	pygame.draw.line( board, color, (30, posY), (WIDTH - 30, posY), 15)

def draw_asc_diagonal(player):
	if player == 1:
		color = WHITE
	elif player == 2:
		color = BLACK

	pygame.draw.line( board, color, (30, HEIGHT - 30), (WIDTH - 30, 30), 15 )

def draw_desc_diagonal(player):
	if player == 1:
		color = WHITE
	elif player == 2:
		color = BLACK

	pygame.draw.line( board, color, (30, 30), (WIDTH - 30, HEIGHT - 30), 15 )

def restart():
    board.fill(GREEN )
    draw_lines()
    board_arr = np.zeros((ROWS, COLUMNS)) 

def is_full():
    for row in range(ROWS):
	    for col in range(COLUMNS):
		    if board_arr[row][col] == 0:
			    return False
   
    return True


player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not is_full():
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            row_clicked = int(mouseY // 200)
            col_clicked = int(mouseX // 200)

            if is_block_available(row_clicked, col_clicked):
               if player == 1:
                   player_mark(row_clicked, col_clicked, 1)
                   draw_figure(row_clicked, col_clicked)
                   if check_winner(player):
                       gameover = True
                   player = 2
               elif player == 2:
                   player_mark(row_clicked, col_clicked, 2)
                   draw_figure(row_clicked, col_clicked)
                   if check_winner(player):
                       gameover = True
                   player = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r :
                restart()
                player = 1
                game_over = False


    pygame.display.update()
