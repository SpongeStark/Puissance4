import random

class Player:
  def __init__(self,signal=1,name="untitled",ishuman=True):
    self.signal = signal
    self.name = name
    self.isHuman = ishuman
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

  def getOneStep(self,min,max):
    if self.isHuman:
      return self.getOneStep_fromTerminal(min,max)
    return self.getOneStep_fromRandom(min,max)

  def reset(self):
    self.nbStep = 0