# !/usr/bin/env python
#coding:utf-8

import random
import collections

#用蓄水池算法模拟从10个数中随机抽取一个数
def reservoir():
    raw_list = [0,1,2,3,4,5,6,7,8,9]
    ret_num = raw_list[:6] #蓄水池初始化。因为只需要抽取一个，所以给一个变量即可

    for i in range(6,10): #从第k+1个元素开始遍历
        m = random.randint(1,i+1) #因为列表下标从0开始，所以随机数上限为i+1而不是i
        if m < 6:
            ret_num[m] = raw_list[i] #蓄水池里的元素替换

    return ret_num

#抽取十万次，看看最后的结果
def run():
    dic = collections.defaultdict(int)
    for i in range(100000):
        ret_num = reservoir()
        dic[ret_num] += 1

    for k,v in dic.items():
        print(k,":",v)

# run()
print(reservoir())
import random
if True:
    m_list = [int(i) for i in input().split()]
    n = int(input())
    ret_list = m_list[:n]

    for i in range(n,10):
        m = random.randint(1,i+1)
        if m < n:
            ret_list[m] = m_list[i]
'''
先将前n个数取出来放入结果集中，然后从第n+1个数开始遍历。假设遍历到第i个数，以n/i的概率替换掉j结果集中的某个元素即可
'''








