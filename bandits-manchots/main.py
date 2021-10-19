from algos import *
import numpy as np

def apply_algos(N, T, num_algo):
    '''运用四个算法，分别用1，2，3，4编号 |
       appliquer les 4 algos, qui sont numérosés par 1,2,3 et 4'''
    if num_algo not in [1,2,3,4]:
        return
    N_t = [0] * N # N_t (i)
    mu_t = [0] * N # mu_t (i)
    for t in range(0,T):
        if num_algo == 1:
            (mu_t, N_t) = algo_random(mu_t, N_t)
        elif num_algo == 2:
            (mu_t, N_t) = algo_greedy(mu_t, N_t)
        elif num_algo == 3:
            (mu_t, N_t) = algo_epsilon_greedy(mu_t, N_t)
        elif num_algo == 4:
            (mu_t, N_t) = algo_UCB(mu_t, N_t)
    return mu_t

def get_decision(N,T,num_algo):
    mu_hat = apply_algos(N,T,num_algo)
    return mu_hat.index(max(mu_hat))

def array_round(myList):
    '''保留四位小数 | garder 4 décimales'''
    return [float('{:.4f}'.format(i)) for i in myList]

def main():
    N = 650 # 臂的数量 | nombre de leviers
    T = 100 # 总学习次数 | nombre de fois total d'apprentissage 
    length = 800 # 验证结果执行总次数 | nombre de fois pour vérifier la statistique du résultat de 4 algos
    # print("Random : ", array_round(apply_algos(N,T,1)))
    # print("Greedy : ", array_round(apply_algos(N,T,2)))
    # print("epsilon-Greedy : ", array_round(apply_algos(N,T,3)))
    # print("UCB : ", array_round(apply_algos(N,T,4)))
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
        


if __name__ == "__main__":
    main()

