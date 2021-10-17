from Player import Player
import random


class RandomPlayer(Player):

    def __init__(self, signal=1, name="untitled"):
        super().__init__(signal, name)

    def getOneStep(self, game):
        # print(self.name,"has finished one step")
        return random.choice(game.get_available_columns())
