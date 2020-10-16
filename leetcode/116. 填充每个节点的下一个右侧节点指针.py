# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        point = root
        queue = [point,"NULL"]

        while queue:
            tem = queue.pop(0)
            if tem != "NULL":
                if tem.left:
                    queue += [tem.left, tem.right]
                tem.next = queue[0]
            else:
                if len(queue) != 0:
                    queue.append("NULL")


        return root


a = [1, 2, 3, 4, 5, 6, 7]
root = Node(a.pop(0))

point = root

queue = [point]

while queue:
    tem = queue.pop(0)
    if a:
        tem.left = Node(a.pop(0))
    else:
        break
    if a:
        tem.right = Node(a.pop(0))
    queue += [tem.left, tem.right]

s = Solution()
s.connect(root)
