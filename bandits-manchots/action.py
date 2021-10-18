import random
import csv

def one_action(leviers, a_t):
    '''第一题：执行一次拉杆操作，返回1或者0，表示gain或者lost'''
    n = random.random()
    if n < leviers[a_t]:
        return 1
    return 0

def get_data(path,head=False):
    result = []
    # 读取CSV文件
    data = list(csv.reader(open(path)))
    # 清除表头
    if head:
        del data[0]
    # 开始读取数据，并转化成小数
    for item in data:
        temp = float(item[0])
        result.append(temp)
    return result

def action(i):
    '''设定很多很多个老虎机作为数据库，执行拉杆操作'''
    # leviers = [0.8753,0.1348,0.6507,0.2307,
    #             0.2895,0.3162,0.2681,0.1990,
    #             0.5475,0.6850,0.3121,0.9555,
    #             0.4289,0.5359,0.9913,0.1589,
    #             0.1007,0.4551,0.8026,0.2781]
    leviers = get_data(path='./data.csv', head = True)
    return one_action(leviers,i)