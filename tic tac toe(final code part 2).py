board_arr = np.zeros((ROWS, COLUMNS))


def player_mark(row, col, player):
    board_arr[row][col] = player


def is_block_available(row, col):
    return board_arr[row, col] == 0


def draw_figure(row, col):
    #drawing "O"
    if board_arr[row][col] == 1:
        pygame.draw.circle(board, WHITE, (int(col * 200 + (200 / 2)), int(row * 200 + (200/2))), CIRCLE_RADIUS, CIRCLE_WIDTH)
    #drawing "X"
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
