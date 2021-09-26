#!/usr/bin/python3

from Game import Game
import numpy as np

BOARD_LENGTH = 7
BOARD_HEIGHT = 6
PLAYER1 = 1
PLAYER2 = -1

oneGame = Game(BOARD_HEIGHT,BOARD_LENGTH)
# oneGame.run(PLAYER1,PLAYER2)
oneGame.run_with_random()

