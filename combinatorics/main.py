#!/usr/bin/python3

# from Player import Player
from Game import Game
import numpy as np
import matplotlib.pyplot as pyplot

from RandomPlayer import RandomPlayer
from HumanPlayer import HumanPlayer
from MonteCarloPlayer import MonteCarloPlayer
from UCTPlayer import UCTPlayer

BOARD_LENGTH = 7
BOARD_HEIGHT = 6
PLAYER1 = 1
PLAYER2 = -1

def count_and_analyze(player1,player2,num_round=100):
    oneGame = Game(BOARD_HEIGHT, BOARD_LENGTH)
    nb_coups_max = BOARD_HEIGHT*BOARD_LENGTH//2+1
    countWin_player1 = [0]*(nb_coups_max)
    countWin_player2 = [0]*(nb_coups_max)
    player1_win = 0
    player2_win = 0
    nb_tie = 0 #nobody win the game

    for i in range(0,num_round):
        if i%2 == 0:
            result = oneGame.run(player1,player2,showChessBoard=False)
        else:
            result = oneGame.run(player2,player1,showChessBoard=False)
        if not result == 0 :
            if result.signal == player1.signal:
                countWin_player1[result.nbStep] += 1
                player1_win += 1
            elif result.signal == player2.signal:
                countWin_player2[result.nbStep] += 1
                player2_win += 1
        else:
            nb_tie += 1

    print(player1.name,"won",countWin_player1,"in total",player1_win,"times")
    print(player2.name,"won",countWin_player2,"in total",player2_win,"times")
    print("there are ",nb_tie,"ties during the games, and the probability is",nb_tie/num_round) #times of tie

    proba1 = np.array(countWin_player1)/num_round
    proba2 = np.array(countWin_player2)/num_round
    pyplot.bar(np.arange(nb_coups_max)+0.8,proba1,width=0.4,label=player1.name,color='r')
    pyplot.bar(np.arange(nb_coups_max)+1.2,proba2,width=0.4,label=player2.name,color='b')
    pyplot.xlabel('nb_de_coups')
    pyplot.ylabel('probabilite')
    pyplot.legend(loc="upper left")
    pyplot.show()

def part1():
    #print(np.size(oneGame.get_win_board(),0))
    #on a une liste de 69 quadruplets de cases
    player1 = RandomPlayer(signal=PLAYER1, name="Random1")
    player2 = RandomPlayer(signal=PLAYER2, name="Random2")
    count_and_analyze(player1,player2,10000)

def part2():
    #MonteCarlo VS Random:
    player1 = MonteCarloPlayer(signal=PLAYER1, name="MonteCarlo")
    player2 = RandomPlayer(signal=PLAYER2, name="Random")
    count_and_analyze(player1,player2,100)
    #MontreCarlo VS MontreCarlo:
    player1 = MonteCarloPlayer(signal=PLAYER1, name="MonteCarlo1")
    player2 = MonteCarloPlayer(signal=PLAYER2, name="MonteCarlo2")
    count_and_analyze(player1,player2,100)

def part3():
    #MonteCarlo VS UCTPlayer:
    player1 = MonteCarloPlayer(signal=PLAYER1, name="MonteCarlo", simulation_times=100)
    player2 = UCTPlayer(signal=PLAYER2, name="UCT",  simulation_times=100 ,first=20)
    count_and_analyze(player1,player2,200)

if __name__ == "__main__":
    # part1()
    # part2()
    part3()
