#!/usr/bin/python3

# from Player import Player
from Game import Game
# import numpy as np
# import matplotlib.pyplot as pyplot

from RandomPlayer import RandomPlayer
from HumanPlayer import HumanPlayer
from MonteCarloPlayer import MonteCarloPlayer

BOARD_LENGTH = 7
BOARD_HEIGHT = 6
PLAYER1 = 1
PLAYER2 = -1
NUM_ROUND = 10

oneGame = Game(BOARD_HEIGHT, BOARD_LENGTH)
# oneGame.run(PLAYER1,PLAYER2)
player1 = HumanPlayer(signal=PLAYER1, name="YK")
player2 = MonteCarloPlayer(signal=PLAYER2, name="GYH")
oneGame.run(player1, player2)

# countWin_player1 = [0]*(BOARD_HEIGHT*BOARD_LENGTH//2+1)
# countWin_player2 = [0]*(BOARD_HEIGHT*BOARD_LENGTH//2+1)
# player1_win = 0
# player2_win = 0
# nb_tie = 0 #nobody win the game
#
# for i in range(0,NUM_ROUND):
#     result = oneGame.run(player1,player2,showChessBoard=False)
#     if not result == 0 :
#         if result.signal == player1.signal:
#             countWin_player1[result.nbStep] += 1
#             player1_win += 1
#         elif result.signal == player2.signal:
#             countWin_player2[result.nbStep] += 1
#             player2_win += 1
#     else:
#         nb_tie += 1

# print(player1.name,"won",countWin_player1,"in total",player1_win,"times")
# print(player2.name,"won",countWin_player2,"in total",player2_win,"times")
# print("there are ",nb_tie,"ties during the games, and the probability is",nb_tie/NUM_ROUND) #times of tie


# pyplot.plot(countWin_player1)
# pyplot.plot(countWin_player2)
# pyplot.show()
