def restart():
    board.fill(GREEN)
    draw_lines()
    for row in range(ROWS):
	    for col in range(COLUMNS):
		    board_arr[row][col] = 0


draw_lines()

def is_full():
    for row in range(ROWS):
	    for col in range(COLUMNS):
		    if board_arr[row][col] == 0:
			    return False
    return True

player = 1
game_over = False
num1 = 0
num2 = 0

#main()
while True:
    #for pressing the key
    for event in pygame.event.get():
        #detecting QUIT key
        if event.type == pygame.QUIT:
            sys.exit()
            
        # detecting mouse's clicks
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not is_full():
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            row_clicked = int(mouseY // 200)
            col_clicked = int(mouseX // 200)
