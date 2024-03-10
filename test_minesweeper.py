import pytest
from functions_minesweeper import *
def test_count_adjacent_mines_in_corner():
    board = ['X', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',]
    count = count_adjacent_mines(board,0,4)
    assert(count == 0)

def test_insert_mines():
    #write a single unit test insert mines
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
    board, mine_selected = play_turn(board, 4,4)
    assert board == ['O', 'O', 'O', 'O', 'O',
                     'O', 'O', 'X', 'O', 'O',
                     'O', 'X', 'O', 'X', 'O',
                     'O', 'O', 'X', 'O', 'O',
                     'O', 'O', 'O', 'O', '#',]
    assert mine_selected == True


    # board is a segment of memory allocated from a bigger memory
    # when u initialise board that's = to that memory segment
    # when u call that board it then updates with the bottom
