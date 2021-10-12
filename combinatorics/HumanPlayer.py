from Player import Player


class HumanPlayer(Player):

    def __init__(self, signal=1, name="untitled"):
        super().__init__(signal, name)

    def getOneStep(self, game):
        left = 0
        right = game.nCol - 1
        while True:
            myInput = input(self.name + " : ")
            try:
                result = int(myInput)
                if result < left or result > right:
                    print("Out of border\nRetry")
                    continue
                else:
                    return result
            except ValueError:
                print("Retry")
