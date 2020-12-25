# Definition for a binary tree node.
from typing import List


class BTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = [3, 9, 20, None, None, 15, 7]


def createBinaryTree(initial: [int]) -> BTree:
    head = BTree(initial.pop(0))
    queue = [head]

    while initial:
        i = queue.pop(0)
        i.left = BTree(initial.pop(0)) if initial[0] is not None else initial.pop(0)
        i.right = BTree(initial.pop(0)) if initial[0] is not None else initial.pop(0)
        if i.left:
            queue.append(i.left)
        if i.right:
            queue.append(i.right)
    return head


root = createBinaryTree([])


class Solution:
    def zigzagLevelOrder(self, root: BTree) -> List[List[int]]:
        if not root: return []
        direction = 0
        queue = [[root]]
        res = []
        while queue:
            tem = queue.pop()
            second = []
            node_list = []
            while tem:
                node = tem.pop()
                second.append(node.val)
                if direction == 0:
                    if node.left is not None:
                        node_list.append(node.left)
                    if node.right is not None:
                        node_list.append(node.right)
                else:
                    if node.right is not None:
                        node_list.append(node.right)
                    if node.left is not None:
                        node_list.append(node.left)
            direction = 1 if direction == 0 else 0
            res.append(second)
            if node_list:
                queue.append(node_list)
        return res


s = Solution()
print(s.zigzagLevelOrder(BTree()))
