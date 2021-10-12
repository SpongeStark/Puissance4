
from Player import Player
import random

class RandomPlayer(Player):

  def __init__(self,signal=1,name="untitled"):
    super().__init__(signal,name)

  def getOneStep(self, game):
    min = 0
    max = game.nCol-1
    # print(self.name,"has finished one step")
    return random.randint(min,max)