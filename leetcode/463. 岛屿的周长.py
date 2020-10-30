from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dp = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = [0, 0]
        used = set()

        def dfs(x, y):
            if grid[x][y] != 1:
                return
            res[1] += 1
            for i in dp:
                new_x, new_y = x+i[0], y+i[1]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                    res[0] += 1
                    if (new_x, new_y) not in used:
                        used.add((new_x, new_y))
                        dfs(new_x, new_y)
        for i in range(len(grid)):
            if 1 in grid[i]:
                index = grid[i].index(1)
                used.add((i,index))
                dfs(i, index)
                break
            else:
                continue
        print(res)
        return 4 * res[1] - res[0]


# nums = [[0, 1, 0, 0],
#         [1, 1, 1, 0],
#         [0, 1, 0, 0],
#         [1, 1, 0, 0]]
nums = [[1,1]]

s = Solution()

s.islandPerimeter(nums)


# fixme 节省一半的时间  ：由于岛屿内没有湖,所以只需要求出 北面(或南面) + 西面(或东面)的长度再乘2即可

class Solution1:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        prm = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    if j == 0 or grid[i][j - 1] == 0:
                        prm += 1
                    if i == 0 or grid[i - 1][j] == 0:
                        prm += 1
        return prm * 2


