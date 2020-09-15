# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


class Solution:
    def inorderTraversal(self, root):
        if not root: return []
        res = []
        stack = []

        def dfs(root):
            stack.append(root.val)
            if root.left:
                dfs(root.left)
            res.append(stack.pop())
            if root.right:
                dfs(root.right)

        if root:
            dfs(root)
        return res


s = Solution()
print(s.inorderTraversal(root))


def XianXu(root):
    if root == None:
        return
    print(root.val)
    XianXu(root.left)
    XianXu(root.reft)


def ZhongXu(root):
    if root == None:
        return
    ZhongXu(root.left)
    print(root.val)
    ZhongXu(root.reft)


def HouXu(root):
    if root == None:
        return
    HouXu(root.left)
    HouXu(root.reft)
    print(root.val)
