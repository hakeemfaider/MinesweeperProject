import pytest
from functions_minesweeper import *
def test_count_adjacent_mines_in_corner(): #testing adjacent mines edge case
    board = ['X', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',]
    count = count_adjacent_mines(board,0,4)
    assert(count == 0)

def test_insert_mines(): #write a single unit test insert mines
    board = ['O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',]
    insert_mines(board, [[0, 0], [0,4], [4,0], [4,4]])
    assert (board == ['X', 'O', 'O', 'O', 'X',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O',
                      'X', 'O', 'O', 'O', 'X',])

def test_count_adjacent_mines():
    board = ['O', 'O', 'O', 'O', 'O',
             'O', 'O', 'X', 'O', 'O',
             'O', 'X', 'O', 'X', 'O',
             'O', 'O', 'X', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',]
    mine_count = count_adjacent_mines(board, 2, 2)
    assert mine_count == 4

def test_play_turn():
    board = ['O', 'O', 'O', 'O', 'O',
             'O', 'O', 'X', 'O', 'O',
             'O', 'X', 'O', 'X', 'O',
             'O', 'O', 'X', 'O', 'O',
             'O', 'O', 'O', 'O', 'X',]
    board, mine_selected = play_turn_board(board, 4,4)
    assert board == ['O', 'O', 'O', 'O', 'O',
                     'O', 'O', 'X', 'O', 'O',
                     'O', 'X', 'O', 'X', 'O',
                     'O', 'O', 'X', 'O', 'O',
                     'O', 'O', 'O', 'O', '#',]
    assert mine_selected == True

def test_check_win():
    board = ['_', '_', '1', '_', '_',
             '_', '2', 'X', '2', '_',
             '1', 'X', '4', 'X', '1',
             '_', '2', 'X', '2', '1',
             '_', '_', '1', '1', 'X',]
    game_status = check_win(board)
    assert game_status == True

#all single unit test(s) complete