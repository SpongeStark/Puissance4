import random
from Player import Player
# import numpy as np
import copy

from RandomPlayer import RandomPlayer


class MonteCarloPlayer(Player):

    def __init__(self, signal=1, name="untitled"):
        super().__init__(signal, name)

    # def next_step_player(self, game, *players):
    #     s = np.sum(game.myBoard)
    #     # for player in players:
    #     #   if not player.signe==s:
    #     #     return player
    #     if players[0].signal == s:
    #         return players[1]
    #     return players[0]

    def getOneStep(self, game):
        # print("Monte")
        tab = [0] * game.nCol
        n = 100
        # next_player = self.next_step_player(game,*players)
        player1 = RandomPlayer(signal=-self.signal)
        player2 = RandomPlayer(signal=self.signal)
        for i in range(n):
            game_copy = copy.deepcopy(game)
            x = i % game.nCol
            # 如果下满了，就直接continue
            if not game_copy.play(x, self):
                continue
            # 如果接下来的一步就能赢，那就不用模拟了，直接下就完事了
            if game_copy.has_won():
                # tab[x] += 1
                # continue
                return x
            # 开干！！！
            result = game_copy.run(player1, player2, showChessBoard=False, showResult=False, showWarnings=False, restart=False)
            if not result == 0: # 平局
                if result.signal == self.signal: # 自己赢了✌️
                    tab[x] += 1
        # 打印模拟对战的结构
        # print(tab)
        if sum(tab) == 0: # 赢不了了（菜啊）
            # 直接随机出一个数
            return random.randint(0, game.nCol - 1)
        # 返回最大值的下标，即赢的次数最多的列
        return tab.index(max(tab))
