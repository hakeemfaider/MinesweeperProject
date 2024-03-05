def initialise_board():
    # Creating the board (initialisation)
    '''
    Arguments (Inputs):
     - N/A
    Returns (Outputs):
     - A 1x25 row list, therefore total of 25 items which each item being a string 'O' (capital letter O, not number)
    Pre-conditions:
     - N/A
    Post-conditions:
     - The output must be a list containing 25 items (length 25), each element must be a string data type (str)
    '''
    board = ['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
    return board

def display_board(board):
    # Printing the board into 5x5 matrix (Ensuring its hidden)
    '''
    Arguments (Inputs):
    - The list from previous function (1x25)
    Returns (Outputs):
    - N/A however a board which the user can see without mines ('X')
    Pre-conditions:
    - The board must be a list containing 25 items (length 25), each element must be a string data type (str)
    Post-conditions:
    - The new board has a linear relationship of going from row,columns to the 1x25 row list as (5 * row) + column
    - where row value must be 0 <= row <= 4
    - where column value must be 0 <= column <= 4
    '''
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

def insert_mines(board, positions):
    # Adding the mines to the board
    '''
    Arguments (Inputs):
    - The 1x25 row list representing the board
    - A nested list representing the mine location in the format (row, column)
    Returns (Outputs):
    - N/A The output just adds the mine to the list but the user will not able to see the mines as the display_board function hides the mines ('X')
    Pre-conditions:
    - The board must be a list containing 25 items (length 25), each element must be a string data type (str)
    - where row input value must be 0 <= row <= 4
    - where column input value must be 0 <= column <= 4
    Post-conditions:
    - amount of mines < 25 as that's the size of the board
    - The new board has a linear relationship of going from row,columns to the 1x25 row list as (5 * row) + column
    '''
    for i in range(len(positions)):
        position = positions[i]
        row = position[0]
        col = position[1]
        location = (5 * row) + col
        board[location] = 'X'
    return board

def count_adjacent_mines(board, row_check, col_check):
    # Counting adjacent mines using simple linear algorithm
    '''
    Arguments (Inputs):
    - The 1x25 row list representing the board
    - an integer representation the ROW within range (0:4) 0 and 4 inclusive
    - an int representation with the COLUMN within range (0:4) 0 and 4 inclusive
    Returns (Outputs): An int number indicating the number of adjacent lines to that respective row and column position
    Pre-conditions:
    - The board must be a list containing 25 items (length 25), each element must be a string data type (str)
    - where row input value must be 0 <= row <= 4
    - where column input value must be 0 <= column <= 4
    Post-conditions:
    - the adjacent mines no. at the position must be <= 4 (as we are not accounting for diagonal)
    '''
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
    # Playing a turn (entering row, columns to actually start playing minsweeper)
    '''
    Arguments (Inputs):
    - The 1x25 row list representing the board
    - an integer representation the ROW within range (0:4) 0 and 4 inclusive
    - an int representation with the COLUMN within range (0:4) 0 and 4 inclusive
    Returns (Outputs):
    - An int list of the updated board
    - An bool variable type True or False if the mine was selected or not respectively
    Pre-conditions:
    - The board must be a list containing 25 items (length 25), each element must be a string data type (str)
    - where row input value must be 0 <= row <= 4
    - where column input value must be 0 <= column <= 4
    Post-conditions:
    - Boolean variable can only be true or false
    - The board must contain 25 items (length 25), with each element being a string (str)
    - The board has a linear relationship of going from row,columns to the 1x25 row list as (5 * row) + column
    '''
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

#Checking for if the user has beat the game
def check_win(board):
    # Checking for if the user has beat the game
    '''
    Arguments (Inputs):
    - The 1x25 row list representing the board
    Returns (Outputs):
    - a boolean variable type true or false if the game has been won and lost respectively
    Pre-conditions:
    - The board must be a list containing 25 items (length 25), each element must be a string data type (str)
    Post-conditions:
    - Boolean variable can only be true or false
    '''
    game_status = True #initialising boolean data type initially as win, because they haven't done anything to lose yet

    if 'O' in board:
        game_status = False #doesn't necessarily mean they have lost, they just have not played enough turns to determine the result

    # elif '#' in board:
    #     game_status = False #they hit a mine, hence they lost the game

    return game_status

def play_game(positions):
    # Playing the game entirely (putting all functions together, asking the user for input(s) etc)
    '''
    Arguments (Inputs):
    - nested list indicating positions where you want the mines to be placed
    Returns (Outputs):
    - N/A just returns all the functions and the game is ready to be played
    Pre-conditions
    - The board must be a list containing 25 items (length 25), each element must be a string data type (str)
    - where row input value must be 0 <= row <= 4
    - where column input value must be 0 <= column <= 4
    - the user must enter a row and column respectively in the format: "1 2" (ensuring they're within range of the 5x5 grid)
    Post-conditions:
    - The board must contain 25 items (length 25), with each element being a string (str)
    - The mine(s) must be hidden (respective to how many mines were placed) (replaced with a 'O')
    - The no. of adjacent mines must show (<= 4 is max) as the most possible adjacent mines in our context is 4
    - There must be an empty ' ' (space) indicating a clear position with no adjacent mines (not including diagonally)
    - There must be an input repeatingly asking for your row and column to play your turn UNTIL you either win or lose
    - If you win there will be a kind message, elese a message saying try again!
    '''
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