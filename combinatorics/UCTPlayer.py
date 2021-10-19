from math import sqrt,log
from Player import Player
import random
from RandomPlayer import RandomPlayer
import copy


class UCTPlayer(Player):
  
    def __init__(self, signal=1, name="untitled", simulation_times=50, first=10):
        super().__init__(signal, name)
        self.num_sim = simulation_times
        self.first = first
    
    def division_array(self,array_mem, array_denom):
        '''计算两个数组之间的除法 | faire la division entre deux list'''
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
    
    def getArgMax(self,mu_t,N_t,t):
        '''需要最大化的函数'''
        my_func = []
        N = len(mu_t)
        for i in range(0,N):
            if N_t[i] == 0:
                my_func.append(0)
            else:
                my_func.append(mu_t[i] + sqrt( 2 * log(t) / N_t[i]))
        return my_func.index(max(my_func))

    def getOneStep(self, game):
        # print("UCT")
        # 初始化一些标识符 | initialiser les longeurs
        N = game.nCol
        T = self.num_sim
        # 初始化一些中间变量 | initialiser les variable intermédiaire
        a = []
        # N_t (i)
        N_t = [0] * N
        # mu_t (i)
        mu_t = [0] * N
        # r(t)
        r = [0] * T
        gain = [0] * game.nCol
        total = [0] * game.nCol
        # 获得可以进行落子的列 | obtenir les colonnes valables
        available_columns = game.get_available_columns()
        # 初始化两个随机Player | initialiser deux joueurs
        player1 = RandomPlayer(signal=-self.signal)
        player2 = RandomPlayer(signal=self.signal)
        # 开始迭代过程 | commencer le proccess d'itération
        for t in range(T):
            # 做一个副本 | faire un copy de jeu
            game_copy = copy.deepcopy(game)
            if t < self.first :
                # 从可以落子的列中，随机选一个,并放进a[t]里 | choisir une colonne au hasard, et mettre dans a[t]
                a.append(random.choice(available_columns))
            else:
                a.append(self.getArgMax(mu_t, N_t, t-1))
            # 把选出来的结果放进N_t[i] | mettre le résultat dans N_t
            N_t[a[t]] += 1
            # 先下一局 | placer une pièce d'abord dans la colonne choisie
            game_copy.play(a[t], self)
            # 如果接下来的一步就能赢，那就不用模拟了，直接下就完事了
            # si l'on a gagné déjà, pas besion de continuer
            if game_copy.has_won():
                return a[t]
            # 开干！！！ | On y va !!! 
            result = game_copy.run(player1, player2, showChessBoard=False, showResult=False, restart=False)
            # 开始总结 | jury
            if not result == 0: # 如果不是平局 | si c'est pas une partie nulle
                # 先把当前的游戏局数增加一个 | incrémenter le nombre de fois total
                total[a[t]] += 1 
                if result.signal == self.signal: # 自己赢了 | si c'est soi-même qui gagne
                    gain[a[t]] += 1
            # 计算mu_t (i) | calcule mu_t
            if total[a[t]] != 0:
                mu_t[a[t]] = gain[a[t]] / total[a[t]]

        if sum(gain) == 0: # 赢不了了（菜啊）| Si jamais gagner
            # 直接随机出一个数 | choisir au hazard
            return random.choice(available_columns)
        # 返回最大值的下标，即赢的概率最大的列
        # retourner l'indece de max, ça vaut dire le colonne où la prba est la plus grande
        return mu_t.index(max(mu_t))