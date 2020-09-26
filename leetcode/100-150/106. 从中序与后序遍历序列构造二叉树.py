# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        if not inorder or not postorder: return []

        def dfs(pre_list, pro_list, point):
            if pro_list:
                point.val = pro_list.pop(-1)
                index = pre_list.index(point.val)
                if index == 0 and len(pre_list) == 1: return point
                pre = pre_list[index - 1] if index != 0 else pre_list[index]
                pro = pre_list[index + 1] if index < len(pre_list) - 1 else pre_list[index]

                point.left = dfs(pre_list[:pre_list.index(pre) + 1], pro_list[:pro_list.index(pre) + 1],
                                 TreeNode(point.left))

                point.right = dfs(pre_list[pre_list.index(pro):], pro_list[pro_list.index(pro):], TreeNode(point.right))

            return point

        point = root = TreeNode(postorder[-1])
        dfs(inorder, postorder, point)
        return root


# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]

# inorder = [2, 1]
# postorder = [2, 1]

inorder = [1, 2]
postorder = [2, 1]

s = Solution()
s.buildTree(inorder, postorder)
