class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        ans = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                # print(dp)
        print(ans)
        return ans


s = Solution()

a = "asdfasdf"
b = "asdffasdf"
s.longestCommonSubsequence(a, b)


def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'

    res = ["-1"]

    def get_res(flag, a, x, y):
        if x == 0 or y == 0:
            return
        if flag[x][y] == 'ok':
            get_res(flag, a, x - 1, y - 1)
            res[0] += a[x - 1]
        elif flag[x][y] == 'left':
            get_res(flag, a, x, y - 1)
        else:
            get_res(flag, a, x - 1, y)

    get_res(flag, a, lena, lenb)

    return res[0]


a = ""
b = ""
# a = "1A2C3D4B56"
# b = "B1D23CA45B6A"
flag = lcs(a, b)
print(flag)

pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 8, 6]


class Node():
    def __init__(self, x):
        self.v = x
        self.left = None
        self.right = None


def main(p: list, t: list) -> list:
    def getTree(pre, tin):
        if not pre:
            return None
        root = Node(pre[0])
        root_index = tin.index(pre[0])
        root.left = getTree(pre[1:1 + root_index], tin[:root_index])
        root.right = getTree(pre[1 + root_index:], tin[root_index + 1:])
        return root

    tree = getTree(p, t)
    res = []

    def postTravel(root):
        if not root:
            return None
        postTravel(root.left)
        postTravel(root.right)
        res.append(root.v)

    postTravel(tree)
    return res


print(main(pre, tin))
