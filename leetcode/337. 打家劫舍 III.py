list1 = [3, 4, 5, 1, 3, None, 1]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(list_tem):
    head = TreeNode(list_tem[0])
    point = head
    queue = [point]
    pro = 1
    while queue and pro < len(list_tem):
        point_tem = queue.pop(0)
        if list_tem[pro] is not None:
            point_tem.left = TreeNode(list_tem[pro])
            queue.append(point_tem.left)
        if list_tem[pro + 1] is not None:
            point_tem.right = TreeNode(list_tem[pro + 1])
            queue.append(point_tem.right)
        pro += 2
    return head


root = build_tree(list1)


def rob(root) -> int:
    def dfs(node):
        if node is None: return [0, 0]
        l, r = dfs(node.left), dfs(node.right)
        used = node.val + l[1] + r[1]
        not_used = max(l[0], l[1]) + max(r[0], r[1])
        return [used, not_used]

    val = dfs(root)

    return max(val[0], val[1])


print(rob(root))
