'''
Author: zzf
Date: 2020-09-16 09:48:56
LastEditors: zzf
LastEditTime: 2020-10-26 15:58:27
Description: python script
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return
        tem = root.left
        root.left = root.right
        root.right = tem
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root


def createBinaryTree(a:list[int]):
    root = TreeNode(a.pop(0))
    queue = [root]
    while a:
        i = queue.pop(0)
        i.left = TreeNode(a.pop(0)) if a[0] is not None else a.pop(0)
        i.right = TreeNode(a.pop(0)) if a[0] is not None else a.pop(0)
        if i.left:
            queue.append(i.left)
        if i.right:
            queue.append(i.right)
    return root


a = [4, 2, 7, 1, 3, 6, 9]
root = createBinaryTree(a)


s = Solution()
b = s.invertTree(root)
print(b)


