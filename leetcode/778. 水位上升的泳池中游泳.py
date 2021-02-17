from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        dp = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = []

        def dfs(x, y, time, used):
            used.add((x, y))

            if x == h - 1 and y == w - 1:
                res.append(time)
                return

            min_ = float("inf")
            min_x, min_y = x, y
            sign = False
            for new_x, new_y in dp:
                new_x, new_y = x + new_x, y + new_y
                if 0 <= new_x < h and 0 <= new_y < w and (new_x, new_y) not in used:
                    sign = True
                    if time >= grid[new_x][new_y]:
                        dfs(new_x, new_y, time, used)
                        sign = False
                    else:
                        if grid[new_x][new_y] < min_:
                            min_x, min_y = new_x, new_y
                            min_ = grid[new_x][new_y]

            if sign:
                dfs(min_x, min_y, min_, used)
            else:
                return

        dfs(0, 0, max(grid[0][0], grid[-1][-1]), set())

        return min(res)


# a = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
# a = [[0,2],[1,3]]
a = [[10, 12, 4, 6], [9, 11, 3, 5], [1, 7, 13, 8], [2, 0, 15, 14]]
s = Solution()
print(s.swimInWater(a))
