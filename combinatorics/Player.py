import random


class Player:
    def __init__(self, signal=1, name="untitled"):
        self.signal = signal # 1 ou -1
        self.name = name
        self.nbStep = 0 # nombre de coup

    def getOneStep(self, game):
        # print(self.name, "has finished one step")
        return random.choice(game.get_available_columns())

    def reset(self):
        self.nbStep = 0
