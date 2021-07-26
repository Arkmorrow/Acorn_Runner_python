"""
A simple program that will import your tests and run them all!
Be sure you include tests for your other modules like cells and player!

Usage: python3 test_all.py
"""

import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_get_position import run_tests as test_get_position
from test_grid import run_tests as test_grid

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")


#test game
print('Test_game:')
test_game()
print()

#test grid
print('Test_grid:')
test_grid()
print()

#test parser
print('Test_parser:')
test_parser()
print()

#test get position
print('Test_get_position:')
test_get_position()
print()

# Run the e2e script
subprocess.call(['./test_e2e.sh'])
