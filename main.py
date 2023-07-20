from constants import *
from gui import Sudoku
from threading import Event

from solver import Solver

def main():

    game = Sudoku()
    game.run()


if  __name__ == '__main__':
    main()