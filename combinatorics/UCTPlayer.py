from Player import Player
import random
from RandomPlayer import RandomPlayer
import copy


class UCTPlayer(Player):
  
    def __init__(self, signal=1, name="untitled"):
        super().__init__(signal, name)

    def getOneStep(self, game):
        # print("UCT")
        N = game.nCol
        T = 100
        tab = [0] * game.nCol
        # next_player = self.next_step_player(game,*players)
        player1 = RandomPlayer(signal=-self.signal)
        player2 = RandomPlayer(signal=self.signal)
        for i in range(T):
            game_copy = copy.deepcopy(game)
            x = i % game.nCol
            # 如果下满了，就直接continue
            if not game_copy.play(x, self):
                continue
            # 如果接下来的一步就能赢，那就不用模拟了，直接下就完事了
            if game_copy.has_won():
                return x
            # 开干！！！
            result = game_copy.run(player1, player2, showChessBoard=False, showResult=False, showWarnings=False, restart=False)
            if not result == 0: # 平局
                if result.signal == self.signal: # 自己赢了✌️
                    tab[x] += 1
        # 打印模拟对战的结果
        # print(tab)
        if sum(tab) == 0: # 赢不了了（菜啊）
            # 直接随机出一个数
            return random.randint(0, game.nCol - 1)
        # 返回最大值的下标，即赢的次数最多的列
        return tab.index(max(tab))