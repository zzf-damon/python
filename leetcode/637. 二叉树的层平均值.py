from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = [0]
root = TreeNode(a.pop(0))
queue = [root]

while a:
    i = queue.pop(0)
    i.left = TreeNode(a.pop(0))
    i.right = TreeNode(a.pop(0))
    queue.append(i.left)
    queue.append(i.right)


class Solution:
    def averageOfLevels(self, root):
        res = []
        if root.val == None:
            return res
        queue = [root]
        while queue:
            sum, count = 0, 0
            tem_list = []
            for i in queue:
                if i.val is not None:
                    count += 1
                    sum += i.val
                    if i.left:
                        tem_list += [i.left]
                    if i.right:
                        tem_list += [i.right]
            res.append(sum/count)
            queue = tem_list
        return res


class b():
    def __init__(self):
        sef.name = b


s = Solution()
print(s.averageOfLevels(root))
