import os
import os
import json


# path = os.path.abspath('..')
# file_path = "result/result2.txt"
# path1 = os.path.join(path, file_path)
# f = open(path1, "w")
# word = f.write("asdfas")
# # /home/z/code/py/TopJudge-master/data_processor/result
# print(word)

# module_path = os.path.dirname(__file__)
# filename = module_path + filename

#
# import os
# print (os.getcwd()) #获取当前工作目录路径
# print (os.path.abspath('.') )#获取当前工作目录路径
# print (os.path.abspath('test.txt')) #获取当前目录文件下的工作目录路径
# print (os.path.abspath('..')) #获取当前工作的父目录 ！注意是父目录路径
# print( os.path.abspath(os.curdir) )#获取当前工作目录路径


# str = """{"meta": {"crit": ["盗窃"], "time": {"youqi": [4], "guanzhi": [], "huanxing": [], "juyi": [], "sixing": false, "wuqi": false}, "criminals": ["颜某"], "law": [[264, 0, 0]]}, "fact": [["公诉", "机关", "指控", "：", ", "元"], ["案", "发", "后", "，", "被告人", "颜某", "家", "属", "已", "赔偿", "被害人", "全部", "损失", "年", "以下", "××", "、", "××", "或者", "××", "，", "并", "处", "罚金"], []]}"""
# data = json.loads(str)
# print(data)

"""
import tensorflow as tf
from util.gmf import PairwiseGMF
with open('text1.txt', 'r') as f1:
    list1 = f1.readlines()
with open('text2.txt', 'r') as f2:
    list2 = f2.readlines()

print(len(list2))
for i in range(len(list2)):
    if(list1[i] == list2[i]):
        print(list1[i], list2[i])
    else:
        print(i)
        break


"""

# %%
import json, os, requests

filename = "./test.txt"


def read_dict(filename):
    with open(filename, "r") as pf:
        datas = pf.readlines()
    return datas


datss = []
datas = read_dict(filename)
for data in datas:
    dict = json.loads(data)
    datss.append(dict["YQBT"])


# %%

def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    print(list)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new


if __name__ == "__main__":
    test_report = "./static/log/"  # 目录地址
    new_report(test_report)

# %%  获取时间
import datetime

nowTime = datetime.datetime.now().strftime('%Y-%m-%d')  # 现在5
print(nowTime)

# 读取jsondict
import json, re

filename = r"./test1.txt"


def read_dict(filename):
    with open(filename, "r") as pf:
        datas = pf.readlines()
    return datas


datss = []
datas = read_dict(filename)

for data in datas:
    dict = json.loads(data, encoding="GBK")
    datss.append(dict["YQBT"])
print(datss)
# %% 删除目录
import shutil
import os
import glob

dir = "./static/log/"
shutil.rmtree(dir)
os.mkdir(dir)
