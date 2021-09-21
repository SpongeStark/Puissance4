#!/usr/bin/python3

import numpy as np

arr1 = np.array([(1,2,3,4),(1,2,3,4)])
arr1 = np.append(arr1,np.array([(1,2,3,4)]), axis=0)
# arr1 = np.append(arr1,[(1,2,3,4)])
print(arr1)