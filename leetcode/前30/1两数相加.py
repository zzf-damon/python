class ListNode:
    def __init__(self, x=None, y=None):
        self.val = x
        self.next = y


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = ListNode(0)
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        if (carry > 0):
            r.next = ListNode(1)
        return re.next

    def is_empty(self, ln):
        if ln:
            return ListNode(0)

    def LinkSumNode(self, node, signA, l1, l2):
        node.next = ListNode()
        sum = self.get_val(l1) + self.get_val(l2) + signA
        if sum < 10:
            signA = 0
            node.val = sum
        else:
            signA = 1
            node.val = sum % 10
        if l1 or l2 or signA == 1:
            self.LinkSumNode(node.next, signA, l1.next, l2.next)
        else:
            if l1 is not None:
                node.next = l2.next
                return node
            if l2 is not None:
                node.next = l1.next
                return node
        return node


def LinkNode(node, list):
    if node.val is None:
        node.val = list.pop(0)
    if list:
        node.next = ListNode(list.pop(0))
        LinkNode(node.next, list)


if __name__ == "__main__":
    l1 = [5, 9, 9]
    l2 = [5]
    l3 = ListNode()
    l4 = ListNode()
    LinkNode(l3, l1)
    LinkNode(l4, l2)
    solution = Solution()
    solution.addTwoNumbers(l3, l4)


# %%
# fixme 链表
class ListNode:
    def __init__(self, x=None, y=None, l_child=None, r_child=None):
        self.val = x
        self.name = y
        self.l_child = l_child
        self.r_child = r_child


def LinkNode(node, list):
    if node.val is None:
        NODE_VALUE = list.pop(0)
        node.val = NODE_VALUE[0]
        node.name = NODE_VALUE[1]
    if list:
        NODE_VALUE = list.pop(0)
        node.l_child = ListNode(NODE_VALUE[0], NODE_VALUE[1])
        LinkNode(node.l_child, list)
        NODE_VALUE = list.pop(0)
        node.r_child = ListNode(NODE_VALUE[0], NODE_VALUE[1])
        LinkNode(node.r_child, list)


l1 = [(5, "lilei"), (9, "lifang"), (9, "lihuw"), (11, "lihuw1"), (10, "lihuw1"), (13, "lihuw1")]
l4 = ListNode()
LinkNode(l4, l1)
l4
