from multiprocessing import Pool, Queue, Process
import os
import threading
from time import sleep
import time


# from multiprocessing import Queue,process

def write(q):
    print("启动写子进程%s" % os.getpid())
    for i in range(0, 5):
        q.put(str(i))
        print(i)
        sleep(1)
    q.put("这是终极测试")
    print("写子进程结束")


def read(q):
    print("启动度子进程%s" % os.getpid())
    while True:
        value = q.get(True)
        # break
        if value == "这是终极测试":
            print("这是终极测试——————说明读进程应该终止，且value为5")
            break
        else:
            print("value= :" + value)
            t = threading.Thread(target=read_th, args=(value,))
            t.start()
            t.join()
    print("读子进程结束")

#%%
def read_th(i):
    sleep(3)
    print("%s     线程名%s" % (i, threading.current_thread().name))

#%%
if __name__ == '__main__':
    start = time.time()
    print("这是开始的时间%s " % str(start))
    q = Queue()
    pw = Process(target=write, args=(q,))
    print("是什么没有执行")
    pr = Process(target=read, args=(q,))
    print("是什么没有执行")
    pw.start()
    pr.start()
    pr.join()
    end = time.time()
    print("这是最后的时间吗%s" % str(end - start))




