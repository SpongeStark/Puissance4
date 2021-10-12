import random
from Player import Player
import numpy as np
import copy

from RandomPlayer import RandomPlayer

class MonteCarloPlayer(Player):

  def __init__(self,signal=1,name="untitled"):
    super().__init__(signal,name)


  def next_step_player(self, game, *players):
    s = np.sum(game.myBoard)
    # for player in players:
    #   if not player.signe==s:
    #     return player
    if players[0].signal == s :
      return players[1]
    return players[0]

  
  def getOneStep(self, game):
    print("Monte")
    tab=[0] * game.nCol
    N=1000
    # next_player = self.next_step_player(game,*players)
    player1 = RandomPlayer(signal=1)
    player2 = RandomPlayer(signal=-1)
    for i in range(N):
      game_copy = copy.deepcopy(game)
      x = i % game.nCol
      if not game_copy.play(x, self):
        continue
      result = game_copy.run(player1,player2,showChessBoard=False,showResult=False,showWarnings=False,restart=False)
      if not result == 0:
        if result.signal == self.signal :
          tab[x] += 1
    if sum(tab) == 0:
      random.randint(0,game.nCol-1)
    return tab.index(max(tab))
    