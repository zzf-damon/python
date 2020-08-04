# 单文件前台执行代码
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
# 构造不同的headers
"""
import random

headers = {
    # https://github.com/search?q=code generation&type=Issues
    'user-agent': ""
}
agentStr = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
"Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
    "UCWEB7.0.2.37/28/999"
]
agentStr = random.choice(agentStr)
headers['user-agent'] = agentStr
print(headers)
"""
# 判断字符串是否全为字母
"""
for i in str2:
    # print(i)
    if (i >= u'\u0041' and i <= u'\u005a') or (i >= u'\u0061' and i <= u'\u007a'):
        continue
    else:
        print("不全为字母")
"""
# 创建线程
"""
import threading
        t = threading.Thread(target=aaa,args=(i,))
        t.start()
"""
# 中文转为十六进制
"""
import binascii
        str3 = binascii.b2a_hex(i.encode("utf8"))
        str2 = str(str3)
"""
# 字符串拿去规则
str = "asdfgh"
print(str[0:2])
list = [12, 3, 4, 5]
for i in list:
    print(i)
# 格式化代码输出
age = input("age:")
name = input("name:")
info = """
age:{1}

a= 1
b="sunck is a goof man"

name:{0}
""".format(name, age)
print(info)
# 写网页
# f = open('./1.html', mode='w', encoding='utf-8')
# f.write(html)
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

try:
    browser.get("https://wwww.sogou.com")
    input = browser.find_element_by_id('kw')
    input.send_keys('python')
    wait= WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

"""

# 正则
import re
str =""
pattern = re.compile(r'page=(\d+)&')   # 查找数字
result1 = pattern.findall(str)




# 设置函数执行时间
import eventlet,time,sys
eventlet.monkey_patch()


def timeOut():
    print("01")
    time.sleep(10)
    print(10)


time_limit = 5  # set timeout time 3s

try:
    with eventlet.Timeout(time_limit, False):
        print("ERROR")
        timeOut()
        # r = requests.get("https://me.csdn.net/dcrmg", verify=False)
        print('error')
except BaseException:
    print(sys.exc_info())
print('over')




# theme 闭包 当一个函数定义在另一个函数内，且使用到了外部函数的参数。整个代码块称为闭包。当外部参数确定时，内部函数参数可以反复调用。
def num(num):  # 定义函数
    def num_in(nim_in):  # 定义函数
        return num + num_in  # 返回两个参数的和。

    return num_in  # 返回内部函数的引用。（变量名）


a = num(100)  # 将参数为100的函数num接收，并赋值给a，只不过这个返回值是一个函数的引用。等于 a = num_in，注意这里接收的不光是函数本身，还有已经传递的参数。
b = a(100)  # 调用函数a,即num_in，并传递一个参数100，返回值给b。



# theme 动态语言添加属性和方法

class Person():  # 创建一个类
    def __init__(self, name):  # 定义初始化信息。
        self.name = name


li = Person('李')  # 实例化Person('李'),给变量li
li.age = 20  # 再程序没有停止下，将实例属性age传入。动态语言的特点。
Person.age = None  # 这里使用类名来创建一个属性age给类，默认值是None。Python支持的动态属性添加。


def eat(self):  # 定义一个方法，不过这个方法再类之外。
    print('%s正在吃东西。。' % self.name)


import types  # 动态添加方法需要使用tpyes模块。

li.eat = types.MethodType(eat, li)  # 使用types.MethodType，将函数名和实例对象传入，进行方法绑定。并且将结果返回给li.eat变量。实则是使用一个和li.eat方法一样的变量名用来调用。
li.eat()  # 调用外部方法eat()方法。


@staticmethod  # 定义静态方法。
def test():  # 定义静态方法，静态方法可以不用self参数。
    print('这是一个静态方法。')


Person.test = test  # 使用类名.方法名 = test的形式来方便记忆和使用，Person.test其实只是一个变量名，没有特殊的含义。
Person.test()  # 调用test方法。


@classmethod  # 类方法
def test(cls):
    print('这是一个类方法。')


Person.test = test  # 定义一个类属性等于方法名。
Person.test()  # 调用方法。


class test(object):  # 定义一个类。
    __slots__ = ('name', 'age')  # 使用slots来将属性固定，不能进行动态添加修改。


d = {'a': 1, 'b': 4, 'c': 2, 'f': 12}

# 第一种方法，key使用lambda匿名函数取value进行排序
a = sorted(d.items(), key=lambda x: x[1])
a1 = sorted(d.items(), key=lambda x: x[1], reverse=True)

# key使用lambda匿名函数按键进行排序
a2 = sorted(d.items(), key=lambda x: x[0])

# 第二种方法使用operator的itemgetter进行排序
import operator

b1 = sorted(d.items(), key=operator.itemgetter(1))

# 第三种方法讲key和value分装成元祖，在进行排序
f = zip(d.keys(), d.values())
c = sorted(f)

print(a)
print(a1)
print(a2)
print(b1)
print(c)
