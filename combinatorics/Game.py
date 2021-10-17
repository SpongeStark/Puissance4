# import random
import numpy as np
from Player import Player


class Game:

    def __init__(self, num_line, num_column):
        # chessboard
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
                # 全是-1或者全是1，则赢，否则则没有人赢
                return True
        return False

    def play(self, x, player: Player):
        '''如果落子成功，则返回True，否则说明该列已满，或者列序号超出了棋盘，并返回False'''
        # 判断期棋盘是否满了
        if self.is_complete() or x < 0 or x >= self.nCol:
            return False
        # 从第一行开始(index=0)
        i = 0
        # 往nrow行(index=nrow-1)遍历
        while i < self.nRow and self.myBoard[i][x] == 0:
            i += 1
            # 如果遍历到了最后一行，或者遇到非0（已落子），则跳出循环
        # 选择已落子的位置的前一个空位进行落子
        i -= 1
        # 如果整列都已落子，也就是说while没有执行，则有大问题！！！
        if i == -1:
            return False
        # 此处落子
        self.myBoard[i, x] = player.signal
        # 并将步数加一
        player.nbStep += 1

        return True
    
    def get_available_columns(self):
        columns = []
        for i in range(self.nCol):
            if self.myBoard[0][i] == 0:
                columns.append(i)
        return columns

    def is_finished(self):
        return self.is_complete() or self.has_won()

    # def run_old(self, player1: Player, player2: Player):
    #     while True:
    #         # input player 1
    #         x = player1.getOneStep()
    #         while not self.play(x, player1):
    #             x = int(input("player 1 (again):"))
    #         print(self.myBoard)
    #
    #         if self.has_won():
    #             print("Player 1 won")
    #             break
    #         elif self.is_complete():
    #             print("END")
    #             break
    #
    #         # input player 2
    #         x = int(input("player 2 :"))
    #         while not self.play(x, player2):
    #             x = int(input("player 2 (again):"))
    #         print(self.myBoard)
    #
    #         if self.has_won():
    #             print("Player 2 won")
    #             break
    #         elif self.is_complete():
    #             print("END")
    #             break

    # def run_with_random(self):
    #     while True:
    #         # input player 1
    #
    #         self.play(random.randint(0, self.nCol - 1), -1)
    #
    #         if self.has_won():
    #             print("Computer won")
    #             break
    #         elif self.is_complete():
    #             print("END")
    #             break
    #
    #         # input player 2
    #         x = int(input("player :"))
    #         while not self.play(x, 1):
    #             x = int(input("player (again):"))
    #         print(self.myBoard)
    #
    #         if self.has_won():
    #             print("Player won")
    #             break
    #         elif self.is_complete():
    #             print("END")
    #             break

    def run(self, *players: Player, showChessBoard=True, showResult=True, restart=True):
        if restart:
            self.reset(players)
        while True:
            for player in players:
                # 落子
                self.play(player.getOneStep(self), player)
                # show棋盘
                if showChessBoard:
                    print(self.myBoard)
                # 游戏判断机制
                if self.has_won():
                    if showResult:
                        print(player.name, "won")
                    return player
                elif self.is_complete():
                    if showResult:
                        print("END")
                    return 0
