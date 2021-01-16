from typing import List
import collections


class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}

    def get_size_of_set(self, x):
        """
        获取所在连通块的大小
        """
        return self.size_of_set[self.find(x)]

    def find(self, x):
        root = x

        while self.father[root] != None:
            root = self.father[root]

        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            # 更新根节点连通块数量
            self.size_of_set[root_y] += self.size_of_set[root_x]
            del self.size_of_set[root_x]

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.size_of_set[x] = 1


class Solution:
    def __init__(self):
        self.CEILING = (-1, -1)
        self.DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def initialize(self, uf, m, n, grid, hits):
        """
        初始化
        """
        # 添加天花板
        uf.add(self.CEILING)

        # 敲掉所有要敲掉的砖块
        for x, y in hits:
            grid[x][y] -= 1

        # 连接，合并剩余的砖块
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uf.add((i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.merge_neighbors(uf, m, n, grid, i, j)

        # 与天花板合并
        for j in range(n):
            if grid[0][j] == 1:
                uf.merge((0, j), self.CEILING)

    def is_valid(self, x, y, grid, m, n):
        return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

    def merge_neighbors(self, uf, m, n, grid, x, y):
        """
        与上下左右的砖块合并
        """
        for dx, dy in self.DIRECTION:
            nx, ny = x + dx, y + dy
            if not self.is_valid(nx, ny, grid, m, n):
                continue
            uf.merge((x, y), (nx, ny))

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        uf = UnionFind()
        m, n = len(grid), len(grid[0])
        res = [0] * len(hits)

        # 初始化
        self.initialize(uf, m, n, grid, hits)

        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]

            # 还原敲击
            grid[x][y] += 1

            # 敲的地方原本就不是砖块
            if grid[x][y] != 1:
                continue

            # 敲完以后与天花板连接的数量
            after_hit = uf.get_size_of_set(self.CEILING)

            # 填回砖块，合并
            uf.add((x, y))
            self.merge_neighbors(uf, m, n, grid, x, y)
            if x == 0:
                uf.merge((x, y), self.CEILING)

            # 被敲的地方和天花板连接
            if uf.is_connected((x, y), self.CEILING):
                # 敲之前和天花板连接的数量
                before_hit = uf.get_size_of_set(self.CEILING)
                res[i] = before_hit - after_hit - 1
        return res


grid = [[1, 0, 0, 0], [1, 1, 0, 0]]
hits = [[1, 1], [1, 0]]

s = Solution()

print(s.hitBricks(grid, hits))


class Solution1:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        res = []  # 存储结果的列表
        current = 0  # 稳定的砖块的数量
        # 先敲掉砖块
        for i, j in hits:
            grid[i][j] -= 1
        # 初始化(标记稳定的砖块)
        for j in range(len(grid[0])):
            visit(0, j, grid)
        # 从后往前恢复砖块
        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]
            grid[x][y] += 1  # 恢复砖块
            # 敲掉的位置原本就不是砖块，掉落0个
            if not grid[x][y]:
                res.append(0)
                continue
            # 没有直接或间接与顶部相连，即不是稳定的砖块(和它相邻的必然也不是稳定的，故掉落0个)
            if x != 0 and not judge(x - 1, y, grid) + judge(x + 1, y, grid) + judge(x, y - 1, grid) + judge(x, y + 1,
                                                                                                            grid):
                res.append(0)
                continue
            current = visit(x, y, grid)  # 与当前位置相连接的稳定的砖块数量
            res.append(current - 1)  # 减1是减去自身
        res.reverse()
        return res


def visit(i, j, grid) -> int:
    # 非法的坐标或者当前位置不是砖块，返回0，即没有稳定的砖块
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return 0
    grid[i][j] += 1  # 标记一下该砖块是不是稳定的
    return visit(i - 1, j, grid) + visit(i + 1, j, grid) + visit(i, j - 1, grid) + visit(i, j + 1, grid) + 1


# 判断该位置是不是稳定的砖块
def judge(i, j, grid) -> int:
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 2:
        return 1
    return 0









