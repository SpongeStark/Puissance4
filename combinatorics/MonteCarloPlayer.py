import random
from Player import Player
import copy
from RandomPlayer import RandomPlayer


class MonteCarloPlayer(Player):

    def __init__(self, signal=1, name="untitled", simulation_times=50):
        super().__init__(signal, name)
        self.num_sim = simulation_times


    def division_array(self,array_mem, array_denom):
        '''计算两个数组之间的除法'''
        result = []
        length = min(len(array_mem), len(array_denom))
        for i in range(length):
            if array_denom[i] == 0:
                if array_mem[i] == 0:
                    result.append(0)
                else:
                    result.append(float('inf'))
            else:
                result.append(array_mem[i] / array_denom[i])
        return result

    def getOneStep(self, game):
        # print("Monte")
        gain = [0] * game.nCol
        total = [0] * game.nCol
        available_columns = game.get_available_columns()
        n = self.num_sim
        player1 = RandomPlayer(signal=-self.signal)
        player2 = RandomPlayer(signal=self.signal)
        for i in range(n):
            # 做一个副本 | faire un copy de jeu
            game_copy = copy.deepcopy(game)
            # 从可以落子的列中，随机选一个 | choisir une colonne au hasard
            x = random.choice(available_columns)
            # 先下一局 | placer une pièce d'abord dans la colonne choisie
            game_copy.play(x, self)
            # 如果接下来的一步就能赢，那就不用模拟了，直接下就完事了
            # si l'on a gagné déjà, pas besion de continuer
            if game_copy.has_won():
                return x
            # 开干！！！ | On y va !!! 
            result = game_copy.run(player1, player2, showChessBoard=False, showResult=False, restart=False)
            if not result == 0: # 如果不是平局 | si c'est pas une partie nulle
                # 先把当前的游戏局数增加一个 | incrémenter le nombre de fois total
                total[x] += 1 
                if result.signal == self.signal: # 自己赢了✌️ | si c'est soi-même qui gagne
                    gain[x] += 1
        if sum(gain) == 0: # 赢不了了（菜啊）| Si jamais gagner
            # 直接随机出一个数  | choisir au hazard
            return random.choice(available_columns)
        # 算出每一列赢的概率 probs <- gain / total
        probs = self.division_array(gain,total)
        # 返回最大值的下标，即赢的次数最多的列
        # retourner l'indece de max, ça vaut dire le colonne où la prba est la plus grande
        return probs.index(max(probs))


