# fixme lambda argument_list: expression
# argument_list是参数列表

# fixme with
class Demo(object):
    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("enter...")
        return self

    def echo_hello(self):
        print("Hello, Hello...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit...")


with Demo() as d:
    d.echo_hello()

import contextlib

a = 0


# 使用装饰器
@contextlib.contextmanager
def file_open(num):
    global a
    a += num
    # 此处写__enter___函数中定义的代码
    print("enter function code...")
    yield {"num": num}
    # 此处写__exit__函数中定义的代码
    print("exit function code...")


with file_open("json.json") as f:  # f是file_open的返回值 ,其中file_open不能写return 方法
    print(f, type(f))

# enter function code...
# exit function code...
