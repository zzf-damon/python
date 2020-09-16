import sys
from typing import List



n = int(input("输入盒子数"))

list_total = sys.stdin.readline().strip()
list_total = list(map(int, list_total.split(" ")))


def solution(box: List[int]) -> int:
    count = 1
    box = sorted(box)
    pre = box[0]
    for i in box[1:]:
        if i == pre:
            count += 1
        pre = i
    return count


#
# n = 5
# list_total = [5, 3, 5, 52, 4]

print(solution(list_total))
