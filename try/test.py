#!/usr/bin/python3

import csv


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


print(get_data(path='./data.csv',head=True))
