# coding:utf-8
# 顺序存储
class Stack(object):  # 此部分代码过于麻烦，只可学习不可借用
    # 初始化一个栈
    def __init__(self, size):
        self.size = size
        self.num = 0
        self.stack = []

    # 获取栈的长度
    def getSize(self):
        return self.num

    # 输出栈
    def outStack(self):
        for l in self.stack:
            print(l)

    # 进栈
    def appendStack(self, value):
        if self.num >= self.size:
            self.popStack()
        else:
            self.stack.append(value)
            self.num += 1

    # 出栈
    def popStack(self):
        if self.isEmpty():
            print("the stack is empty,no element can be output")
            return
        else:
            topElement = self.stack[-1]
            self.stack.remove(topElement)
            return topElement

    def isEmpty(self):
        if self.num == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.num == self.size:
            return True
        else:
            return False


if __name__ == '__main__':
    pre = Stack(5)
    for i in range(10):
        pre.appendStack(i)
