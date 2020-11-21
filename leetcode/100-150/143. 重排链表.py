# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def dfs(node):
            if node and node.next:
                point = node.next
                tem = node.next
            else:
                return
            while point.next:
                if point.next.next:
                    point = point.next
                else:
                    break

            if tem.next:
                node.next = point.next
                point.next = None
                node = node.next
                node.next = tem
                dfs(node.next)

        dfs(head)

        print(head)

a = [1,2,3,4]

root = ListNode(a.pop(0))
queue = [root]
while queue:
    tem = queue.pop(0)
    if a:
        queue.append(ListNode(a.pop(0)))
        tem.next = queue[0]


s = Solution()
s.reorderList(root)
