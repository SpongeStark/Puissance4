# from abc import abstractmethod
import random

# import Game

class Player:
  def __init__(self,signal=1,name="untitled"):
    self.signal = signal
    self.name = name
    self.isHuman = False
    self.nbStep = 0
  
  def getOneStep_fromTerminal(self,min,max):
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

  def getOneStep_fromRandom(self,min,max):
    print(self.name,"has finished one step")
    return random.randint(min,max)

  # @abstractmethod
  def getOneStep(self, game):
    min = 0
    max = game.nCol-1
    print(self.name,"has finished one step")
    return random.randint(min,max)

  def reset(self):
    self.nbStep = 0