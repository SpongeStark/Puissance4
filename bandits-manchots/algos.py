from math import log, sqrt
from action import action
import random

FIRST = 20
EPSILON = 0.1


def update(mu_t, N_t, a_t, r_t):
    '''一个工具函数，以 a_t 和 r_t 为依据，更新参数 mu_t 和 N_t，并返回(mu_t,N_t)元祖'''
    mu_t[a_t] = ( mu_t[a_t] * N_t[a_t] + r_t ) / ( N_t[a_t] + 1 )
    N_t[a_t] += 1
    return (mu_t,N_t)

def algo_random(mu_t, N_t):
    '''随机算法'''
    i = random.randint(0,len(mu_t)-1)
    return update(mu_t=mu_t, N_t=N_t, a_t=i, r_t=action(i))

def algo_greedy(mu_t, N_t):
    '''greedy算法'''
    first = FIRST
    if sum(N_t) < first:
        # 前几个先执行随机算法
        return algo_random(mu_t, N_t)
    # 从某个数开始，进行最大化求解
    i = mu_t.index(max(mu_t))
    return update(mu_t=mu_t, N_t=N_t, a_t=i, r_t=action(i))

def algo_epsilon_greedy(mu_t, N_t):
    '''epsilon-greedy算法'''
    first = FIRST
    epsilon = EPSILON
    prob = random.random()
    if sum(N_t) < first or prob < epsilon :
        return algo_random(mu_t, N_t)
    i = mu_t.index(max(mu_t))
    return update(mu_t=mu_t, N_t=N_t, a_t=i, r_t=action(i))

def getArgMax(mu_t,N_t,t):
    '''置信区间上界，执行argmax操作'''
    my_func = []
    N = len(mu_t)
    for i in range(0,N):
        if N_t[i] == 0:
            my_func.append(0)
        else:
            my_func.append(mu_t[i] + sqrt( 2 * log(t) / N_t[i]))
    return my_func.index(max(my_func))

def algo_UCB(mu_t,N_t):
    '''UCB算法'''
    first = FIRST
    t = sum(N_t)
    if t < first :
        return algo_random(mu_t, N_t)
    i = getArgMax(mu_t, N_t, t)
    return update(mu_t=mu_t, N_t=N_t, a_t=i, r_t=action(i))
