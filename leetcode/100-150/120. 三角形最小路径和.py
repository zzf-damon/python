triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]


# 深度优先搜索
def minimumTotal(triangle):
    res = []
    if len(triangle) == 1:
        return triangle[0][0]
    m = len(triangle) - 1

    def backup(a, b, path):
        path.append(triangle[a][b])
        if a == m:
            res.append(sum(path))
            return
        for i in range(2):
            backup(a + 1, b + i, path)
            path.pop()

    backup(a=0, b=0, path=[])

    return min(res)


# print(minimumTotal(triangle))


# 动态规划
def minimumTotal1(triangle):
    if len(triangle) == 1:
        return triangle[0][0]

    for i, a in enumerate(triangle[1:]):
        i += 1
        for j, b in enumerate(a):
            triangle[i][j] = b + min(triangle[i - 1][j] if i-1 >= j else triangle[i - 1][j - 1],
                                     triangle[i - 1][j - 1] if j > 0 else triangle[i - 1][j])

    return min(triangle[-1])


# print(minimumTotal1(triangle))


def minimumTotal2(triangle):
    n = len(triangle)
    f = [0] * n
    f[0] = triangle[0][0]

    for i in range(1, n):
        f[i] = f[i - 1] + triangle[i][i]
        for j in range(i - 1, 0, -1):
            f[j] = min(f[j - 1], f[j]) + triangle[i][j]
        f[0] += triangle[i][0]

    return min(f)


minimumTotal2(triangle)


