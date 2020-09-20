class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def construct_tree(pre_order, mid_order):
    if len(pre_order) == 0:
        return None
    root_data = pre_order[0]
    i = mid_order.index(root_data)
    left = construct_tree(pre_order[1: 1 + i], mid_order[:i])
    right = construct_tree(pre_order[1 + i:], mid_order[i + 1:])
    return Node(root_data, left, right)


def levelOrder(root):
    res, level = [], [root]
    while root and level:
        currentNode = []
        nextLevel = []
        for node in level:
            currentNode.append(node.data)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        res.append(currentNode)
        level = nextLevel
    T = []
    res_tem = [T + i for i in res]
    # for i in res:
    #     res_tem += i
    # res_tem = []
    # res_tem = list(map(lambda x: x + res_tem, res))
    return res_tem


if __name__ == '__main__':
    pre_order = [1, 2, 3, 4, 5]
    mid_order = [3, 2, 4, 1, 5]
    root = construct_tree(pre_order, mid_order)
    print(levelOrder(root))
    # print (root.data)
    # print (root.left.data)
    # print (root.right.data)
    # print (root.left.left.data)
    # print (root.left.right.data)
