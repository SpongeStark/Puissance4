#!/usr/bin/python3

import numpy as np

def myFunc(*myArgs):
  sum = 0
  for item in myArgs:
    sum += item
  return sum

print(myFunc(1,2,3.8,4))