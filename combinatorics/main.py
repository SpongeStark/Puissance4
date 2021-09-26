#!/usr/bin/python3

from Player import Player
from Game import Game
import numpy as np

BOARD_LENGTH = 7
BOARD_HEIGHT = 6
PLAYER1 = 1
PLAYER2 = -1

oneGame = Game(BOARD_HEIGHT,BOARD_LENGTH)
# oneGame.run(PLAYER1,PLAYER2)
player1 = Player(signal=PLAYER1,name="YK")
player2 = Player(signal=PLAYER2,name="GYH",ishuman=False)

oneGame.run(player1,player2)

