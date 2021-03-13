def solution(s):
    res = []
    if len(s) < 1: return res
    num = 0
    sign = False
    for pre in s:
        if '0' <= pre <= '9':
            num = num * 10 + int(pre)
            sign = True
        else:
            if sign: res.append(num)
            num = 0
            sign = False
    if sign: res.append(num)
    return sorted(res)


# s = "He15l154lo87wor7l87d"
s = "a0125b1c0d00"
# s = input()
res = solution(s)
for i in res:
    print(i)


# 1
def solution1(nums):
    # if not nums: return nums
    # m, n = len(nums), len(nums[0])
    # res = []
    # for i in range(n):
    #     temp = []
    #     for j in range(m):
    #         temp.append(nums[j][i])
    #     res.append(temp)
    nums = list(zip(*nums))
    for i in range(0, len(nums), 1):
        nums[i] = list(nums[i])
    return nums


# m, n = [int(i) for i in input().split(' ')]
# source = []
# for i in range(m):
#     b = [int(i) for i in input().split(' ')]
#     source.append(b)

# # 3 3
# source = [
#     [1,2,3,5],
#     [4,5,6,6]
# ]
# result = solution1(source)
# for i in result:
#     print(' '.join([str(j) for j in i]))


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# def rob(root: TreeNode):
#     def _rob(root):
#         if not root: return 0, 0  # 偷，不偷
#
#         left = _rob(root.left)
#         right = _rob(root.right)
#         # 偷当前节点, 则左右子树都不能偷
#         v1 = root.val + left[1] + right[1]
#         # 不偷当前节点, 则取左右子树中最大的值
#         v2 = max(left) + max(right)
#         return v1, v2
#
#     return max(_rob(root))


def solution4(nums, edges):


n, m = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
edges = []
for i in range(m):
    edges.append([int(i) for i in input().split()])

solution4(nums, edges)

import collections


def ss(nums, word):
    for j in range(int(nums[0]) - int(nums[1]) + 1):
        dict1 = collections.defaultdict(int)
        a = []
        for i in range(j, j + int(nums[1])):
            dict1[word[i]] += 1
            a.append(word[i])
        # a = sorted(a)
        num = max(dict1.values())  # []
        # for i in range(len(a)):
        #     if dict1[a[i]] == num
        #         print(int(a[i]))
        #         break
        for i in a:
            if dict1[i] == num:
                print(i)
                break


# nums = input().split()
# word = input().split()
nums = [5, 3]
word = [1, 2, 2, 1, 3]
ss(nums, word)
