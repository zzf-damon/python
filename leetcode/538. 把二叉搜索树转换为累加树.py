# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        if not root:
            return root
        tem_list = []

        def dfs(node):
            if not node:
                tem_list.append(node.val)

            if not node.left:
                dfs(node.left)

            if not node.right:
                dfs(node.right)
            sum_tatal = 0
            for i in tem_list:
                if i > node.val:
                    sum += node.val
            node.val = sum_tatal

        dfs(root)

        return root




a = [5,2,13]
root = TreeNode(a.pop(0))
queue = [root]

while a:
    i = queue.pop(0)
    i.left = TreeNode(a.pop(0))
    i.right = TreeNode(a.pop(0))
    queue.append(i.left)
    queue.append(i.right)


s = Solution()
s.convertBST(root)

