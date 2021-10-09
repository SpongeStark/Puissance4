#!/usr/bin/python3

from Player import Player
from Game import Game
import numpy as np
import matplotlib.pyplot as pyplot

BOARD_LENGTH = 7
BOARD_HEIGHT = 6
PLAYER1 = 1
PLAYER2 = -1
NUM_ROUND = 100

oneGame = Game(BOARD_HEIGHT,BOARD_LENGTH)
# oneGame.run(PLAYER1,PLAYER2)
player1 = Player(signal=PLAYER1,name="YK",ishuman=False)
player2 = Player(signal=PLAYER2,name="GYH",ishuman=False)
# oneGame.run(player1,player2)

countWin_player1 = [0]*(BOARD_HEIGHT*BOARD_LENGTH//2+1)
countWin_player2 = [0]*(BOARD_HEIGHT*BOARD_LENGTH//2+1)

for i in range(0,NUM_ROUND):
    result = oneGame.run(player1,player2,showChessBoard=False)
    if not result == 0 :  
        if result.signal == player1.signal:
            countWin_player1[result.nbStep] += 1
        elif result.signal == player2.signal:
            countWin_player2[result.nbStep] += 1

print(player1.name,"won",countWin_player1)
print(player2.name,"won",countWin_player2)


pyplot.plot(countWin_player1)
pyplot.plot(countWin_player2)
pyplot.show()


