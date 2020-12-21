import torch
import torch.nn as nn
import torch.nn.functional as F
import torch


# given a string array words, find the maximum value of length(word[i])*length(word[i]) where the two words do not share common letters.
# You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
# · Example 1:
# Input:["abcw","baz","foo","bar","xtfn","abcdef"]
# Output:16
# Explanation: The two words can be "abcw","xtfn".
# · Example 2:
# Input:["a","ab","abc","d","cd","bcd","abcd"]
# Output:4
# Explanation: The two words can be "ab", "cd"
# · Example 3:
# Input:["a","aa","aaa","aaaa"]
# Output:0


class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [25,15,27,99,18,35,14,66]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i]),


# fixme 思想这是一个三叉树，使用一个深度优先算法进行遍历，就可以了
 # 我发给你了
 # 就是一个树结构
 # 遍历就行了
class Tree():  # 构造一个树
    def __init__(self,x):
        self.val = x
        self.FirstChild = None
        self.SecondChild = None
        self.ThirdChild = None

    def get_child(self):
        if self.FirstChild or self.SecondChild or  self.ThirdChild :
            return True
        else:
            return False

root = Tree("A")  #  编写树
root.FirstChild = Tree("A-1")
root.SecondChild = Tree("A-2")
root.ThirdChild = Tree("A-3")
root.SecondChild.FirstChild = Tree("A-2-1")
root.SecondChild.SecondChild = Tree("A-2-2")
root.SecondChild.ThirdChild = Tree("A-2-3")

def dfs(head,path): #  dfs
    path.append(head.val)
    print("/"+"/".join(path))
    if not head.get_child():
        path.pop()
        return
    if head.FirstChild:
        dfs(head.FirstChild,path)
    if head.SecondChild:
        dfs(head.SecondChild,path)
    if head.ThirdChild:
        dfs(head.ThirdChild,path)


dfs(root,[])











