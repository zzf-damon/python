# coding:utf-8

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]):
        max_ = -float("inf")
        min_ = float("inf")

        i = 1
        sign = False
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                sign = True
            if sign:
                min_ = min(min_, nums[i])
            i += 1
        sign = False
        i = len(nums) - 2
        while i >= 0:
            if nums[i] > nums[i + 1]:
                sign = True
            if sign:
                max_ = max(max_, nums[i])
            i -= 1
        l = 0
        r = len(nums) - 1
        for i in range(len(nums)):
            l = i
            if min_ < nums[i]:
                break

        for i in range(r, 0, -1):
            r = i
            if max_ > nums[i]:
                break

        return l, r if l == 0 and l == len(nums) - 1 else 0


nums = [2, 6, 4, 8, 10, 9, 15]

s = Solution()
print(s.findUnsortedSubarray(nums))


def findsort(nums):
    stack = []
    l = len(nums)
    r = 0
    for i in range(len(nums)):
        while stack and nums[stack[-1]] > nums[i]:
            l = min(l, stack.pop())
        stack.append(i)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            r = max(r, stack.pop())
        stack.append(i)
    return r - l + 1 if r - l > 0 else 0


print(findsort(nums))

# 翻转单词
a = "I love China"
res = " ".join([i[::] for i in a.split(" ")])
print(res)

# 不可变类型为number、string、tuple，可变类型为：list、dict、set
"""
不可变类型：不可变类型的变量在第一次赋值声明的时候，会在内存中开辟一块空间，用来存储这个变量被赋予的值，存放这个值的内存空间就是内存中的一个地址，而这个变量存储的并不是被赋予的值而是存放这个值的内存地址，通过这个地址，变量就可以在内存中取出数据了，所谓不可变就是说，我们不能改变这个数据在内存中的值，所以当我们改变这个变量的赋值时，只是在内存中重新开辟了一块空间，将新的数据存放到新的内存地址里，而原来那个变量就不再引原数据的的内存地址，而是转换为引用新数据的内存地址了。

可变数据类型：当你第一次赋值声明了一个可变数据类型的时候, 同样会在内存中开辟一个空间, 并且将你所赋的数据值放在这块内存中, 然后将这个变量指向数据所在的内存地址, 不同的是, 可变数据类型可以对内存中的数据直接进行修改, 并且不会导致变量引用地址的变化, 但是这种修改仅限于Python中的内置方法, 比如list.append(), list.remove(), dict.pop(), dict.clear()等, 如果要是进行重新赋值的操作的话, 一样会改变变量的地址指向。而且当变量重新指向了新的内存之后，之前的内存也就被自动回收了。
"""

#  python2 和 python3 中 range(100)的区别
"""
Python2中使用内置函数range(100)返回是列表集合。
Python3中内置类range(100)返回是可迭代对象
在Python3中，这样的改变可以避免在Python2中因为range(10000000000)过大，导致占用内存过高的问题，因为在Python2中range得到的列表数据是一次性加载到内存中，而在Python3中range得到的是一个可迭代对象，通过循环获取每一个值。
"""


# list(range(10))


# with语句实质上是一个上下文管理器，with语句后的对象都会有__enter__()和__exit__()方法。在进入到上下文时，会自动调用__enter__()方法，程序正常执行完成，或者出现异常中断的时候，都会调用__exit__()方法。
# open 方法的返回值赋值给变量 f，当离开 with 代码块的时候，系统会自动调用 f.close() 方法， with 的作用和使用 try/finally 语句是一样的。

import torch.nn as nn

nn.Conv2d

import  numpy as np
def im2col(img, ksize, stride, padding):
    ''' :param img: 4D array N,FH,FW,C_{in} :param ksize: tuple (kh,kw) :param stride: :return: '''
    kh, kw = ksize

    p1 = kh // 2
    p2 = kw // 2
    img = np.pad(img, ((p1, p1), (p2, p2), padding), 'constant')
    H, W, C = img.shape
    out_h = (H - kh) // stride + 1
    out_w = (W - kw) // stride + 1
    col = np.empty((out_h * out_w, kw * kh * C))
    outsize = out_w * out_h
    for y in range(out_h):
        y_min = y * stride
        y_max = y_min + kh
        y_start = y * out_w
        for x in range(out_w):
            x_start = x * stride
            x_end = x_start + kw
            col[y_start + x::outsize, :] = img[y_min:y_max, x_start:x_end, :].reshape(-1)
    return col

img=np.zeros((300,300,3),dtype=np.uint8)
ksize = (3,3)
stride = 3
padding = ksize
print(im2col(img,ksize,stride,padding))


def conv(X, W, stride=1, padding='same'):
    ''' :param X: 4D array N,FH,FW,C_{in} :param W: 4D array C_{out},kh,kw,C_{in} :param stride: :param padding: :return: 4D array N,F,H,C_{out} '''
    FN, kh, kw, c = W.shape
    N, FH, FW, C = X.shape
    if padding == 'same':
        out_h = FH // stride
        col = im2col(X, (kh, kw), stride)
        z = np.dot(col, W.reshape(FN, -1).T)
        return z.reshape(N, out_h, -1, FN)
