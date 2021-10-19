# import random
import numpy as np
from Player import Player


class Game:

    def __init__(self, num_line, num_column):
        self.nRow = num_line
        self.nCol = num_column
        self.myBoard = np.zeros((num_line, num_column), dtype=np.int)
        self.winBoard = self.get_win_board()

    def is_complete(self):
        for line in self.myBoard:
            for item in line:
                if item == 0:
                    return False
        return True

    def reset(self, players):
        '''reinitialiser la plateau (jeu) et les joueurs'''
        self.myBoard = np.zeros((self.nRow, self.nCol), dtype=np.int)
        for player in players:
            player.reset()

    def get_win_board(self):
        result = np.empty((0, 4, 2), dtype=np.int)
        for i in range(0, self.nRow):
            for j in range(0, self.nCol):
                if i + 3 < self.nRow:
                    temp = np.array([[(i, j), (i + 1, j), (i + 2, j), (i + 3, j)]])
                    result = np.append(result, temp, axis=0)
                if j + 3 < self.nCol:
                    temp = np.array([[(i, j), (i, j + 1), (i, j + 2), (i, j + 3)]])
                    result = np.append(result, temp, axis=0)
                if i + 3 < self.nRow and j + 3 < self.nCol:
                    temp = np.array([[(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)]])
                    result = np.append(result, temp, axis=0)
                if i + 3 < self.nRow and j - 3 >= 0:
                    temp = np.array([[(i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)]])
                    result = np.append(result, temp, axis=0)
        return result

    def has_won(self):
        for line in self.winBoard:
            cnt = 0
            for point in line:
                cnt += self.myBoard[point[0], point[1]]
            if np.abs(cnt) == 4:
                # 全是-1或者全是1，则赢，否则则没有人赢 | gagné si qutre -1 ou qutre 1, sinon personne ne gagner
                return True
        return False

    def play(self, x, player: Player):
        '''落子 | un coup'''
        # 判断期棋盘是否满了 | verifier la validation du nombre de colone
        if self.is_complete() or x < 0 or x >= self.nCol:
            return False
        # 从第一行开始(index=0) | commencer par la première ligne
        i = 0
        # 往nrow行(index=nrow-1)遍历 | parcourir ver la ligne nrow
        while i < self.nRow and self.myBoard[i][x] == 0:
            # 如果遍历到了最后一行，或者遇到非0（已落子），则跳出循环
            # si l'on arrive à la fin, ou rencontre un non-zéro (déjà existe une pièce), alore on sort le boucle
            i += 1
        # 选择已落子的位置的前一个空位进行落子
        # déplacer dans la dernière place où il y a une pièce
        i -= 1
        if i == -1:
            # 如果整列都已落子，也就是说while没有执行，则有大问题！！！
            # si toute la colone est plein, c-à-d le while est jamais exécuté, alors il y a un problème
            return False
        # 此处落子 | placer une pièce ici
        self.myBoard[i, x] = player.signal

        return True
    
    def get_available_columns(self):
        '''retourner tous les colones où on peut placer une pièce'''
        columns = []
        for i in range(self.nCol):
            if self.myBoard[0][i] == 0:
                columns.append(i)
        return columns

    def is_finished(self):
        return self.is_complete() or self.has_won()

    def run(self, *players: Player, showChessBoard=True, showResult=True, restart=True):
        if restart:
            self.reset(players)
        while True:
            for player in players:
                # 落子 | faire une action
                self.play(player.getOneStep(self), player)        
                # 并将步数加一 | et ajouter un coup
                player.nbStep += 1
                # show棋盘 | afficher la plateau
                if showChessBoard:
                    print(self.myBoard)
                # 游戏判断机制 | la jury du résultat
                if self.has_won():
                    if showResult:
                        print(player.name, "won")
                    # retourner le gagnante
                    return player
                elif self.is_complete():
                    if showResult:
                        print("END")
                    return 0
