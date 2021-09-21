#!/usr/bin/python3

import numpy as np

BOARD_LENGTH = 7
BOARD_HEIGHT = 6


def get_all_case_to_win_from_empty_board() :
  result = np.array([[],[],[],[]])
  for i in range(0,BOARD_LENGTH):
    for j in range(0,BOARD_HEIGHT):
      # i+3 < BOARD_LENGTH?
      isGoodForLength = (i+3<BOARD_LENGTH)
      # j+3 < BOARD_HEIGHT?
      isGoodForHeight = (j+3<BOARD_HEIGHT)
      if isGoodForLength :
        temp = np.array([[i,j],[i+1,j],[i+2,j],[i+3,j]])
        result = np.append(result,temp, axis=0)
      # if isGoodForHeight :
      #   temp = np.array([(i,j),(i,j+1),(i,j+2),(i,j+3)])
      #   result = np.append(result,temp, axis=0)
      # if isGoodForLength and isGoodForHeight :
      #   temp = np.array([(i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3)])
      #   result = np.append(result,temp, axis=0)
  return result

print(get_all_case_to_win_from_empty_board())

  