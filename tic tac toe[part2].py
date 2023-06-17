def draw_lines():
    pygame.draw.line(board, RED, (30, 200), (570, 200), 5)
    pygame.draw.line(board, RED, (30, 400), (570, 400), 5)
    pygame.draw.line(board, RED, (200, 30), (200, 570), 5)
    pygame.draw.line(board, RED, (400, 30), (400, 570), 5)
    pygame.draw.line(board, RED, (0, 0), (0, 600), 15)
    pygame.draw.line(board, RED, (0, 0), (600, 00), 15)
    pygame.draw.line(board, RED, (600, 0), (600, 600), 15)
    pygame.draw.line(board, RED, (0, 600), (600, 600), 15)

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
