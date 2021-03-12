from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        pass


words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
s = Solution()
s.findNumOfValidWords(words, puzzles)

import collections


# Definition for a binary tree node.‘


class TreeNode(object):  # 定义树  需要写这个
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#  写完，假装检查一下
class Solution(object):
    def levelOrder(self, root):  # 例如  1 2 3
        queue = collections.deque()  # 队列  先入先出
        queue.append(root)
        res = []
        while queue:  # 如果队列不为空   这就是一个层序遍历的思想，   一层一层遍历就行了
            # 就用一个队列，把遍历到的节点，的子节点放到队列里，如果队列不为空，继续遍历
            size = len(queue)
            level = []
            for _ in range(size):  # 整体就是一个层序遍历的思想
                cur = queue.popleft()  # 这个特有的方法
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)  # 把每一层的结果输出
        return res  # 返回的结果是 [[1],[2,3]]


def createBinaryTree(a):  #
    root = TreeNode(a.pop(0))
    queue = [root]  # 是的  队列   ，一个一个创建就行了

    while a:
        i = queue.pop(0)  #
        i.left = TreeNode(a.pop(0)) if a[0] is not None else a.pop(0)
        i.right = TreeNode(a.pop(0)) if a[0] is not None else a.pop(0)
        if i.left:
            queue.append(i.left)
        if i.right:
            queue.append(i.right)
    return root


a = [4, 2, 7, 1, 3, 6, 9]  # 输入必须是一个list
root = createBinaryTree(a)
s = Solution()
print(s.levelOrder(root))
