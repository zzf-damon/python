# **kwargs是用来将关键字参数打包成字典给函数调用的，kwargs即是传给函数所构成的字典
# *args 是用来将参数打包成元组给函数调用的，args即是传给函数的参数所构成的元组
# arg就是指一个参数
import functools


# 装饰器
def robust(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except:
            print('Error execute: %s' % actual_do.__name__)
            # traceback.print_exc()

    return add_robust


import traceback
import sys
from pprint import pprint


def robust1(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except Exception as err:
            pprint(traceback.extract_tb(sys.exc_info()[2]))
            print(type(err), ":", err)
            print('程序出错，出错的方法名是: %s' % actual_do.__name__)


    return add_robust


@robust
def passTest(num):
    print(num)


number = 1
passTest(number)


# 装饰器的普通写法
def deco(func):  # 传入原函数并在包装函数里调用
    def wrapper(**kwargs):  # 装饰器中定义和原函数相同参数的包装函数
        print("x-->{}".format(kwargs["a"]))
        a = kwargs["a"] * 2
        result = func(a=a, b=kwargs["b"])  # 把这些参数再传入到原函数中
        print("y-->{}".format(kwargs["b"]))
        result = result * 2
        return result  # 原函数有返回值时，在包装函数中返回

    return wrapper  # 最后返回包装函数


@deco
def add(**kwargs):
    print("x-->{},y-->{}".format(kwargs["a"], kwargs["b"]))
    return kwargs["a"] + kwargs["b"]


print(add(a=3, b=7))


def test(**kwargs):
    print(kwargs["a"])
    # print(a,b)


test(a="1", b="2")


# 将装饰器变成一个方法
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg, *args, **kw):
            print('%s %s():' % (text, func.__name__))
            print(arg, type(arg))
            print(args, *args)
            print(kw, **kw)
            arg = arg * text
            return func(arg, *args, **kw)

        return wrapper

    return decorator


@log(2)
def now(number):
    print(number + 1)
    print('2013-12-25')


now(3)

# fixme 迭代器
from itertools import permutations, combinations, chain

num_list = [1, 4, 9, 5]
for i in permutations(num_list):  # 迭代所有的排列，如何不指定个数，默认为，列表长度
    print(i)
for i in permutations(num_list, 2):  # 迭代所有的排列，如何不指定个数，默认为，列表长度
    print(i)

for i in combinations(num_list, 2):  # 迭代所有的组合，如何不指定个数，默认为，列表长度
    print(i)

# theme enumerate() 枚举
# theme zip() 打包
# 如有 m 个列表 ，zip将m个列表打包成一个 m * mix(list.length) 的矩阵


# zip(*zipped)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 7, 8]
res = zip(a, b, c)
print(1, list(res))  # 如果想要打印的东西是zip，或 map ，只能用list(zip),list(map)打印出来

dict1 = {"name": "tom"}
dict2 = {"age": "18"}
s = dict(zip(dict1, dict2))
print(dict(s))

# theme chain() 输入n个列表，输出一个合并列表,不去重
list1 = chain(a, b, c)
print(list(list1))


# fixme yield 生成器
# 1 是一个return 2 继续执行函数 3

def foo1():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g1 = foo1()  # 当你调用这个函数的时候，你写在这个函数中的代码并没有真正的运行。这个函数仅仅只是返回一个生成器对象。
print(next(g1))  # 并不会执行res = 4 ，而是遇到yield时，就进行返回
print("*" * 20)
print(next(g1))  # 此时，继续接着上次运行的结尾，将 None给res，


def foo2():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g2 = foo2()
print(next(g2))
print("*" * 20)
print(g2.send(7))  # 此时，继续接着上次运行的结尾，将 7给res，


def foo3():
    for i in range(10):
        yield i


g3 = foo3()
print(next(g3))
print(next(g3))
print(next(foo3()))
print(next(foo3()))  # 需要将生成器赋予指针


# fixme DataLoader  自己实现
class DataLoader(object):
    def __init__(self, batch, batch_size):
        self.batch_size = batch_size
        self.batch = batch
        self.index = 0
        self.n_batches = len(batches) // batch_size - 1 if len(batch) % self.batch_size == 0 \
            else len(batches) // batch_size

    def __next__(self):
        if self.index == self.n_batches:
            batch = self.batch[self.index * self.batch_size:len(self.batch)]
        elif self.index > self.n_batches:
            self.index = 0
            raise StopIteration
        else:
            batch = self.batch[self.index * self.batch_size: (self.index + 1) * self.batch_size]
        self.index += 1
        return batch

    def __iter__(self):
        return self


batches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dataset = DataLoader(batches, 2)
for i in dataset:
    print(i)
