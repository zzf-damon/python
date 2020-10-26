n = int(input())

list_num = [int(i) for i in input().split(" ")]


def dfs(number):
    res = 0
    for i in range(1, n + 1):
        res = (number % i) ^ res
    return res


tem_b = 0

for i, a_i in enumerate(list_num):
    tem_b = a_i ^ dfs(i) ^ tem_b

print(tem_b)
