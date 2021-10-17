from Player import Player


class HumanPlayer(Player):

    def __init__(self, signal=1, name="untitled"):
        super().__init__(signal, name)

    def getOneStep(self, game):
        while True:
            myInput = input(self.name + " : ")
            try:
                result = int(myInput)
                if result not in game.get_available_columns():
                    print("Unavailable Column\nRetry")
                    continue
                else:
                    return result
            except ValueError:
                print("Retry")
