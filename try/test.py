#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as pyplot

pyplot.bar(np.arange(5),[0,282/500,0,0,0],width=0.4,label="Random",color='r')
pyplot.bar(np.arange(5),[0,0,427/500,0,0],width=0.4,label="Greedy",color='b')
pyplot.bar(np.arange(5),[0,0,0,414/500,0],width=0.4,label="Epsilon-Greedy",color='y')
pyplot.bar(np.arange(5),[0,0,0,0,417/500],width=0.4,label="UCB",color='g')
pyplot.xlabel('Algorithme')
pyplot.ylabel('probabilité')
pyplot.legend(loc="upper left")
pyplot.show()