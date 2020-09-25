# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:



a = [0, 0, None, 0, None, 0, None, None, 0]

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


s = Solution()
s.minCameraCover(root)
