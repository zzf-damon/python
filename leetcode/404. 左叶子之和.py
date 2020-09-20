# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        isLeafNode = lambda node: not node.left and not node.right

        def dfs(node: TreeNode) -> int:
            ans = 0
            if node.left:
                ans += node.left.val if isLeafNode(node.left) else dfs(node.left)
            if node.right and not isLeafNode(node.right):
                ans += dfs(node.right)
            return ans

        return dfs(root) if root else 0


a = [1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, 10, 11, None, 12]

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
s.sumOfLeftLeaves(root)
