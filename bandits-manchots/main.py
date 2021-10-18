from algos import *
import numpy as np

def apply_algos(N, T, num_algo):
    '''运用四个算法，分别用1，2，3，4编号'''
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
    '''保留四位小数'''
    return [float('{:.4f}'.format(i)) for i in myList]

def main():
    N = 500 # 臂的数量
    T = 500 # 总学习次数
    length = 500 # 验证结果执行总次数
    # print("Random : ", array_round(apply_algos(N,T,1)))
    # print("Greedy : ", array_round(apply_algos(N,T,2)))
    # print("epsilon-Greedy : ", array_round(apply_algos(N,T,3)))
    # print("UCB : ", array_round(apply_algos(N,T,4)))
    decision = [0]*5
    # result = [[0]]*5
    result = np.zeros((5,length),dtype=np.int16)

    for j in range(length):
        for num_algo in range(1,5):
            # 先学习
            decision[num_algo] = get_decision(N,T,num_algo)
            # 再应用
            result[num_algo,j] = action(decision[num_algo])
        print(".", end="")
        if j % 20 == 0:
            print(j,"times")
    
    print(result.sum(axis=1))
        


if __name__ == "__main__":
    main()

