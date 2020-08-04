from tqdm import tqdm
from time import sleep

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func():
    for i in tqdm(list1):
        sleep(0.5)

for i in tqdm(list):
   sleep(1)
   func()