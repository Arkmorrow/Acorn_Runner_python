from grid import grid_to_string
from player import Player
from game_parser import read_lines


def test_grid():

    player=Player(0,2,0)
    assert grid_to_string(read_lines('board_simple.txt'),player) == '**A**\n*   *\n**Y**\n\nYou have 0 water buckets.','Test grid failed'
    print('Test grid passed')

    #edge case
    player=Player(-1,-1,0)

    assert grid_to_string(read_lines('board_simple.txt'),player) == '**X**\n*   *\n**Y*A\n\nYou have 0 water buckets.','Test grid edge failed'
    print('Test grid edge passed')

def run_tests():
    test_grid()
