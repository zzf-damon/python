# -*-coding:utf-8-*-
import matplotlib.pyplot as plt


# THEME 快排
def quicksort(array):
    less = []
    greater = []

    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    return quicksort(less) + [pivot] + quicksort(greater)


array = [4, 9, 0, 45, 2, 6, 8]
array1 = quicksort(array)
print(array1)

# THEME 交换变量
a = 1
b = 2
a, b = b, a
print(a, b)

# THEME 逆序输出
print(array1[::-1])
print(list(reversed(array1)))

# THEME 格式化输出字符串
value = {'name': 'Tom', 'age': '20'}
print('Hello %(name)s, your age is %(age)s !' % value)
import pprint

data = {"goal": [["START", "休 · 劳瑞", "蕾切儿 · 哈伍德"], ["蕾切儿 · 哈伍德", "家人", "休 · 劳瑞"]],
        "knowledge": [["休 · 劳瑞", "评论", "完美 的 男人"], ["休 · 劳瑞", "描述", "医疗剧 中 的 性感 医师"],
                      ["休 · 劳瑞", "出生 日期", "1959 - 6 - 11"], ["休 · 劳瑞", "性别", "男"], ["休 · 劳瑞", "职业", "编剧"],
                      ["休 · 劳瑞", "领域", "明星"], ["蕾切儿 · 哈伍德", "评论", "红 头发 和 古装 最 适合 她 ， 美 的 让 人 心碎 。 请 多 拍 些 大片"],
                      ["蕾切儿 · 哈伍德", "获奖", "香水 _ 提名 _ ( 2007 ； 第33届 ) _ 土星奖 _ 土星奖 - 最佳 女 配角"],
                      ["蕾切儿 · 哈伍德", "家人", "休 · 劳瑞"], ["蕾切儿 · 哈伍德", "性别", "女"], ["蕾切儿 · 哈伍德", "职业", "演员"],
                      ["蕾切儿 · 哈伍德", "领域", "明星"], ["休 · 劳瑞", "评论", "不要 疯狂 迷恋 叔 ， 叔 只是 个 传说 。"], ["休 · 劳瑞", "评分", "9.4"],
                      ["休 · 劳瑞", "星座", "双子座"], ["休 · 劳瑞", "职业", "导演"]],
        "history": ["你 对 明星 有没有 到 迷恋 的 程度 呢 ？", "一般 吧 ， 毕竟 年纪 不 小 了 ， 只是 追星 而已 。"],
        "response": "那 你 喜欢 休 · 劳瑞 不 ？ 一个 外国 明星 。"}
pprint.pprint(data)


# THEME if-elif-else语句的另一种写法,运用字典的形式输出
def f(x):
    return {0: "You typed zero...", 1: "You are in top...", 2: "n is even number...", }.get(x, "Default value")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Tom', 18)


def func(k, x):
    y = x + 1
    dict1 = {
        "y": y,
        "x": x
    }
    return {0: "name = {p.name} age = {p.age}".format(p=p),
            1: "y1={0},y2={0},x ={1}".format(y, x),
            2: "{num1} 总是比{num2}大一".format(num1=y, num2=x),
            3: "{y} 总是比{x}大一".format(**dict1)
            }.get(k)


print(func(0, 2))

# THEME 关于if语句
a, b, c = 1, 2, 3
# 表达式
c = a if a > b else b
# 二维列表
d = [b, a][a > b]  # false ,第一个,true 第二个
d2 = [1, 2][False]
d3 = [1, 2, 3][2]


def test1(number):
    return number


sign = [1, 2, 3][test1(2)]
resu1 = "if" if a < 2 else "else"
x = 3
result = x if (x > 4) else (x - 1)

# [对(x)的操作 for x in 集合 if 条件]
# [对(x,y)的操作 for x in 集合1 for y in 集合2 if 条件] 这里的if语句好像不能跟else
# 生成器与列表更加节省内存
# range(start, end, step)
# [start, end) 包含开头不包含结尾
for i in range(1, 10, 2): print(i)  # python3
for i in range(6): print(i)  # python3

# THEME 索引
num_list = [1, 4, 9]
for i, val in enumerate(num_list): print(i, '-->', val)

# THEME 字符串拼接
names = ['Tom', 'Jack', 'Sam']
''.join(names)

# # THEME 读取文件
# with open('a.txt') as f:
#     data = f.read()

# THEME 列表操作
from collections import deque

names = deque(['c', 'd', 'e'])
names.popleft()  # 左侧出队
names.appendleft('b')  # 左侧进队
names.append('f')  # 后面入队
# names => deque(['b', 'd', 'e', 'f'])

# %%
# THEME 结构赋值
student = ['Tom', 18, 'male']
name, age, gender = student
print(name, age, gender)
# Tom 18 male
# %%
num_list = [100, 19, 20, 98]
first, *left_num_list, last = num_list  # 这里的first,last,就是位置的赋值,没有名字的影响,就是说,first,last,可以交换位置而不影响赋值的改变
print(first, left_num_list, last)
# 100 [19, 20] 98
# %%
student = [['Tom', (98, 96, 100)], ['Jack', (98, 96, 100)]]
print(student)
for name, (first, second, third) in student:
    print(name, first, second, third)
# 字典的遍历  .items
student = {
    'name': 'Tom',
    'age': 18
}
for k, v in student.items():  # 同样的是字典的赋值
    print('k', '-->', v)
# THEME 推导式
# 生成1-100的奇数
odd = [i for i in range(1, 100) if i % 2 == 1]
# 集合a，b分别取一个数，找出和大于10的所有组合
a = [1, 3, 7, 5]
b = [4, 9, 2, 4, 6]
result = [(x, y) for x in a for y in b if x + y > 10]

# fixme for else   在执行玩for循环之后，就会执行else  如果其中有if也不会影响，for循环的级别高于if,只有for循环被break中断的时候才能不执行else


for i in range(3):
    print(i)
else:
    print("else")

# %%

lsit = [(1, 2), (2, 3)]

for i, _ in lsit:
    print(i, _)

from datetime import datetime


def main():
    print("******")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
