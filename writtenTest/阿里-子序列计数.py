"""
1、非递减序列a
2、所有的子序列满足  a_i & a_j = a_i
3、结果对10^9 + 7 取模

1 2 3 7  == 7
1 2 3 7 15 == 18
"""


def solution(n, nums):
    res = [0]
    used = set()

    def dfs(number):
        if nums[number] in used:
            return
        tem_list = nums[number:]
        key = tem_list[0]
        list_tem2 = [key]
        # fixme 构建的数组有问题
        for i in tem_list[1:]:
            if i & list_tem2[-1] == list_tem2[-1]:
                list_tem2.append(i)

        for i in range(len(list_tem2) - 1):
            if list_tem2[i] in used:
                continue
            used.add(list_tem2[i])
            length = len(list_tem2[i + 1:])
            res[0] += 2 ** length - 1

    for i in range(n - 1):
        dfs(i)
    return res[0] % (10 ** 9 + 7)


# n = int(input())
# list1 = [int(i) for i in input().split(" ")]


list1 = [1, 2, 3, 7, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(solution(len(list1), list1))

#  第二种思路

from itertools import combinations

res1 = []

for i in range(2, len(list1)):
    res1 += list(combinations(list1, i))

total = []
count = 0
for i in res1:
    signA = True
    for j in range(len(i)):
        for k in range(j, len(i)):
            if i[j] & i[k] != i[j]:
                signA = False
    if signA:
        count += 1
        total.append(i)

print(count)
print(total)
