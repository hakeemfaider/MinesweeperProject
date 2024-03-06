# import pytest
from functions_minesweeper import *
def test_count_adjacent_mines_in_corner():
    board = ['X', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',
             'O', 'O', 'O', 'O', 'O',]
    count = count_adjacent_mines(board,0,4)
    assert(count == 0)