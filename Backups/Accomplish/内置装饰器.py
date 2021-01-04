# fixme 特性装饰器：@property 可以把一个实例方法变成其同名属性，以支持实例访问，它返回的是一个property属性；
#  在设置属性时，可以对值对进检查，设置发生时，可以 修改设置的值，获取属性时，可以动态地计算值。


import math


class Circle:
    def __init__(self, radius):  # 圆的半径radius
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2  # 计算面积

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius  # 计算周长


# 我们可以通过实例访问到类中属性
circle = Circle(10)
print(circle.radius)
# 通过@property装饰后的方法也可以像访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值；
print(circle.area)
print(circle.perimeter)


# fixme setter是设置属性值。deleter用于删除属性值。而官方文档中给出了getter用于获取属性信息，但是实际使用中可以直接通过property获取属性信息；
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


# 实例化类
c = C()
# 为属性进行赋值
c.x = 100
# 输出属性值
print(c.x)
# 删除属性
del c.x


# fixme @classmethod   修饰的方法不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。


class A():
    number = 10
    number2 = 100

    @classmethod
    def get_a(cls):  # cls 接收的是当前类，类在使用时会将自身传入到类方法的第一个参数
        print('这是类本身：', cls)  # 如果子类调用，则传入的是子类
        print('这是类属性:', cls.number)
        print('这是类1属性:', cls.number2)


class B(A):
    number = 20
    pass


# 调用类方法 不需要实例化可以执行调用类方法
A.get_a()
B.get_a()

# fixme staticmethod：改变一个方法为静态方法，静态方法不需要传递隐性的第一参数，静态方法的本质类型就是一个函数 一个静态方法可以直接通过类进行调用，也可以通过实例进行调用


import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():  # 用Date.now()的形式去产生实例,该实例用的是当前时间
        t = time.localtime()  # 获取结构化的时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday)  # 新建实例并且返回

    @staticmethod
    def tomorrow():  # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


a = Date('1987', 11, 27)  # 自己定义时间
print(a.year, a.month, a.day)
b = Date.now()  # 采用当前时间
print(b.year, b.month, b.day)
c = Date.tomorrow()  # 采用明天的时间
print(c.year, c.month, c.day)
