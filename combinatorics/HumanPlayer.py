
from Player import Player


class HumanPlayer(Player):

  def __init__(self,signal=1,name="untitled"):
    super().__init__(signal,name)

  def getOneStep(self, game):
    min = 0
    max = game.nCol-1
    while True:
      myInput = input(self.name + " : ")
      try:
        result = int(myInput)
        if result<min or result>max:
          print("Out of border\nRetry")
          continue
        else:
          return result
      except:
        print("Retry")