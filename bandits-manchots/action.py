import random
import csv

def one_action(leviers, a_t):
    '''第一题：执行一次拉杆操作，返回1或者0，表示gain或者lost | 
       Exécuter une fois, et retourner 1 si gagné, ou 0 si perdu'''
    n = random.random()
    if n < leviers[a_t]:
        return 1
    return 0

def get_data(path,head=False):
    result = []
    # 读取CSV文件 | lire un fichier csv
    data = list(csv.reader(open(path)))
    # 清除表头 | supprimer le header
    if head:
        del data[0]
    # 开始读取数据，并转化成小数 | lire les donnée ligne par ligne, et convertir à float
    for item in data:
        temp = float(item[0])
        result.append(temp)
    return result

def action(i):
    '''设定很多很多个老虎机作为数据库，执行拉杆操作 | 
       préparer beaucoup de machine à sous (les probas) comme une base de donnée 
       où on prend pour faire une action'''
    leviers = get_data(path='./data2.csv', head = True)
    return one_action(leviers,i)