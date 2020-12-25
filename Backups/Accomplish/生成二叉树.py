class BTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


a = [4, 2, 7, 1, 3, 6, 9]
root = createBinaryTree(a)
