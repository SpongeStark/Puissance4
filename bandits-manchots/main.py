from math import log, sqrt
import random
import numpy as np


def one_action(leviers, a_t):
    n = random.random()
    if n < leviers[a_t]:
        return 1
    return 0

def action(i):
    leviers = [0.8753,0.1348,0.6507,0.2307,
                0.2895,0.3162,0.2681,0.1990,
                0.5475,0.6850,0.3121,0.9555,
                0.4289,0.5359,0.9913,0.1589,
                0.1007,0.4551,0.8026,0.2781]
    return one_action(leviers,i)

def algo_random(N,T):
    gain = 0
    for t in range(0,T):
        a_t = random.randint(0,N-1)
        gain += action(a_t)
    return gain

def algo_greedy(N,T,first):
    a = []
    # N_t (i)
    N_t = [0] * N
    # mu_t (i)
    mu_t = [0] * N
    # r(t)
    r = [0] * T

    for t in range(0,T):
        if t < first :
            # 前几个先随机选一个
            a.append(random.randint(0,N-1))
        else :
            # 从某个数开始，进行最大化求解
            a.append(mu_t.index(max(mu_t)))
        # 把选出的结果，放进N_t (i)里
        N_t[a[t]] += 1
        # action一局，并把结果分别放进r(t)
        r[t] = action(a[t])
        # 计算mu_t (i)
        mu_t[a[t]] = ( mu_t[a[t]] * ( N_t[a[t]] - 1 ) + r[t] ) / N_t[a[t]]
    
    return sum(r)

def algo_epsilon_greedy(N,T,first,epsilon):
    a = []
    # N_t (i)
    N_t = [0] * N
    # mu_t (i)
    mu_t = [0] * N
    # r(t)
    r = [0] * T

    for t in range(0,T):
        prob = random.random()
        if  t < first or prob < epsilon :
            # 前几个先随机选一个, 此后有epsilon的概率随机选一个
            a.append(random.randint(0,N-1))
        else :
            # 有1-epsilon的概率执行greedy算法
            a.append(mu_t.index(max(mu_t)))
        # 把选出的结果，放进N_t (i)里
        N_t[a[t]] += 1
        # action一局，并把结果分别放进r(t)
        r[t] = action(a[t])
        # 计算mu_t (i)
        mu_t[a[t]] = ( mu_t[a[t]] * ( N_t[a[t]] - 1 ) + r[t] ) / N_t[a[t]]
    
    return sum(r)
        

def getArgMax(mu_t,N_t,t):
    my_func = []
    N = len(mu_t)
    for i in range(0,N):
        if N_t[i] == 0:
            my_func.append(0)
        else:
            my_func.append(mu_t[i] + sqrt( 2 * log(t) / N_t[i]))
    return my_func.index(max(my_func))


def algo_UCB(N,T,first):
    a = []
    # N_t (i)
    N_t = [0] * N
    # mu_t (i)
    mu_t = [0] * N
    # r(t)
    r = [0] * T
    # 需要argmax的function
    my_func = [0] * N

    for t in range(0,T):
        if t < first :
            # 前几个先随机选一个
            a.append(random.randint(0,N-1))
        else :
            # 计算my_func 
            # my_func[a[t-1]] = mu_t[a[t-1]] + sqrt( 2 * log(t-1) / N_t[a[t-1]])
            # 从某个数开始，进行最大化求解
            # a.append(my_func.index(max(my_func)))
            a.append(getArgMax(mu_t, N_t, t-1))
        # 把选出的结果，放进N_t (i)里
        N_t[a[t]] += 1
        # action一局，并把结果分别放进r(t)
        r[t] = action(a[t])
        # 计算mu_t (i)
        mu_t[a[t]] = ( mu_t[a[t]] * ( N_t[a[t]] - 1 ) + r[t] ) / N_t[a[t]]
        
        
    
    return sum(r)


def main():
    N = 8
    T = 1000
    first = 20
    epsilon = 0.1
    print("Random : ",algo_random(N,T))
    print("Greedy : ",algo_greedy(N,T,first))
    print("epsilon-Greedy : ",algo_epsilon_greedy(N,T,first,epsilon))
    print("UCB : ",algo_UCB(N,T,first))


if __name__ == "__main__":
    main()

