from algos import *
import numpy as np
import matplotlib.pyplot as pyplot

def apply_algos(N, T, num_algo):
    '''运用四个算法，分别用1，2，3，4编号 |
       appliquer les 4 algos, qui sont numérosés par 1,2,3 et 4'''
    if num_algo not in [1,2,3,4]:
        return
    N_t = [0] * N # N_t (i)
    mu_t = [0] * N # mu_t (i)
    for t in range(0,T):
        if num_algo == 1:
            algo_random(mu_t, N_t)
        elif num_algo == 2:
            algo_greedy(mu_t, N_t)
        elif num_algo == 3:
            algo_epsilon_greedy(mu_t, N_t)
        elif num_algo == 4:
            algo_UCB(mu_t, N_t)
    return mu_t

def get_decision(N,T,num_algo):
    mu_hat = apply_algos(N,T,num_algo)
    return mu_hat.index(max(mu_hat))

def test(N,T):
    length = 800 # 验证结果执行总次数 | nombre de fois pour vérifier la statistique du résultat de 4 algos
    decisions = [0]*5
    result = np.zeros((5,length),dtype=np.int16)

    for j in range(length):
        for num_algo in range(1,5):
            # 先学习 | apprendre d'abord pour obtenir la meilleur moyenne
            decisions[num_algo] = get_decision(N,T,num_algo)
            # 再应用 | et puis appliquer
            result[num_algo,j] = action(decisions[num_algo])
        # 动态打印计算过程 | affichier la progression de calcule
        print(".", end="")
        if j % 20 == 0:
            print(j,"times")
        print()
    # afficher le résultat
    print(result.sum(axis=1)[1:4])

def regret_algos(N, T, num_algo):
    '''获得遗憾值随t的函数 | obtenir le regret en fonction de temps'''
    if num_algo not in [1,2,3,4]:
        return
    N_t = [0] * N # N_t (i)
    mu_t = [0] * N # mu_t (i)
    r = [0] * T
    regret_function = [0] * T
    for t in range(T):
        if num_algo == 1:
            r[t] = algo_random(mu_t, N_t)
        elif num_algo == 2:
            r[t] = algo_greedy(mu_t, N_t)
        elif num_algo == 3:
            r[t] = algo_epsilon_greedy(mu_t, N_t)
        elif num_algo == 4:
            r[t] = algo_UCB(mu_t, N_t)
        regret_function[t] = t * max(mu_t) - sum(r)
    return regret_function

def draw_graph(N,T):
    '''画出遗憾函数图像 | déssiner le graphe avec 4 fonctions de regret'''
    pyplot.plot(np.arange(T),regret_algos(N,T,1),label="random",color='r')    
    pyplot.plot(np.arange(T),regret_algos(N,T,2),label="Greedy",color='b')
    pyplot.plot(np.arange(T),regret_algos(N,T,3),label="Epsilon-greedy",color='y')
    pyplot.plot(np.arange(T),regret_algos(N,T,4),label="UCB",color='g')
    pyplot.xlabel('T')
    pyplot.ylabel('regret')
    pyplot.legend(loc="upper left")
    pyplot.show()

def main():
    N = 650 # 臂的数量 | nombre de leviers
    T = 500 # 总学习次数 | nombre de fois total d'apprentissage 
    
    # test(N,T)
    draw_graph(N,T)

if __name__ == "__main__":
    main()

