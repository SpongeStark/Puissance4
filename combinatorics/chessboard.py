import numpy as np

class Chessboard:

  def __init__(self,num_line, num_colone):
    # chessboard
    self.nRow = num_line
    self.nCol = num_colone
    self.myBoard = np.zeros(num_line,num_colone)
    self.winBoard = self.get_all_case_to_win_from_empty_board()

  def is_complet(self):
    for line in self.myBoard :
      for item in line :
        if item == 0 :
          return False
    return True

  
  def reset(self) :
    self.myBoard = np.zeros(self.nRow,self.nCol)

  def get_all_case_to_win_from_empty_board() :
    result = np.empty((0,4,2))
    for i in range(0,BOARD_LENGTH):
      for j in range(0,BOARD_HEIGHT):
        # i+3 < BOARD_LENGTH?
        isGoodForLength = (i+3<BOARD_LENGTH)
        # j+3 < BOARD_HEIGHT?
        isGoodForHeight = (j+3<BOARD_HEIGHT)
        if isGoodForLength :
          temp = np.array([[[i,j],[i+1,j],[i+2,j],[i+3,j]]])
          result = np.append(result,temp, axis=0)
        if isGoodForHeight :
          temp = np.array([[(i,j),(i,j+1),(i,j+2),(i,j+3)]])
          result = np.append(result,temp, axis=0)
        if isGoodForLength and isGoodForHeight :
          temp = np.array([[(i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3)]])
          result = np.append(result,temp, axis=0)
        if i-3>=0 and j-3 >= 0 :
          temp = np.array([[(i,j),(i-1,j-1),(i-2,j-2),(i-3,j-3)]])
          result = np.append(result,temp, axis=0)
    return result

  def has_won(self) :
    for line in self.winBoard :
      sum = 0
      for point in line :
        sum += self.myBoard[point[0]][point[1]]
      if sum == -4 or sum == 4:
      # 全是-1或者全是1，则赢，否则则没有人赢
        return True
      return False
  
  def play(self,x,player):
    if self.is_complet() :
      return
    i = 0
    while i < self.nRow and self.myBoard[i][x] == 0 :
      i += 1
    self.myBoard[i,x] = player

  def is_finished(self):
    return self.is_complet() or self.has_won()




  
