#Creating the board (initialisation)
def initialise_board():
    board = ['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
    return board

#printing the board into 5x5 matrix
def display_board(board):
    user_board = [] #initialising the list which will be updated version of the official board but with mines hidden
    for imposter in board: #iterating through the original, and offical board
        if imposter == 'X':
            user_board.append('O') #updating the board to change the 'X' to a 'O' to hide the mine
        else:
            user_board.append(imposter) #updating the board to the orignal, official board (essentially copying)

    #printing the board out
    print(user_board[0:5])
    print(user_board[5:10])
    print(user_board[10:15])
    print(user_board[15:20])
    print(user_board[20:25])

#adding the mines to the board
def insert_mines(board, positions):
    for i in range(len(positions)):
        position = positions[i]
        row = position[0]
        col = position[1]
        location = (5 * row) + col
        board[location] = 'X'
    return board

#counting adjacent mines
def count_adjacent_mines(board, row_check, col_check):
    mine_count = 0
    position_to_check = (5 * row_check) + col_check

    # Check the square above, if it exists
    if row_check > 0 and board[position_to_check - 5] == 'X':
        mine_count += 1

    # Check the square below, if it exists
    if row_check < 4 and board[position_to_check + 5] == 'X':
        mine_count += 1

    # Check the square to the left, if it exists
    if col_check > 0 and board[position_to_check - 1] == 'X':
        mine_count += 1

    # Check the square to the right, if it exists
    if col_check < 4 and board[position_to_check + 1] == 'X':
        mine_count += 1

    #print('This square is touching ' + str(mine_count) + ' adjacent mine(s) ( not diagonal though ) ') #just to help me see what the code is doing

    return mine_count

#Playing a turn
def play_turn_board(board, row_check, col_check):
    position_to_check = (5 * row_check) + col_check
    mine_count = count_adjacent_mines(board, row_check, col_check)
    mine_selected = False #initialising boolean variable, as initially no mine would have been chosen

    if board[position_to_check] == 'X':
        board[position_to_check] = '#'
        mine_selected = True
    elif mine_count == 0:
        board[position_to_check] = ' '
    else:
        board[position_to_check] = str(mine_count) #as brief requires mine count to be a string and not an integer data type

    return board, mine_selected

#Checking for win
def check_win(board):
    game_status = True #initialising boolean data type initially as win, because they haven't done anything to lose yet

    if 'O' in board:
        game_status = False #doesn't necessarily mean they have lost, they just have not played enough turns to determine the result

    elif ' ' in board:
        game_status = False #doesn't necessarily mean they have lost, they just have not played enough turns to determine the result

    elif '#' in board:
        game_status = False #they hit a mine, hence they lost the game

    return game_status

#playing the game entirely
def play_game(positions):
    board = initialise_board()
    display_board(board) #using the complimentary function
    insert_mines(board, positions)

    while True:
        user_input = input("Please enter a row and column to play: ")
        row_check, col_check = map(int, user_input.split()) #converting string to int datatype using map function and storing integers as row_check and col_check
        board, mine_selected = play_turn_board(board, row_check, col_check) #returns the updated board and a boolean if a mine has been chosen or not
        display_board(board) #displaying the user's view of the board which is safe to show

        if mine_selected:
            print("Unfortunately you lost, try again!")
            break
        elif check_win(board):
            print("Congratulations, you won!")
            break