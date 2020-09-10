from typing import List
import numpy

numpy.dot



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k == 1:
            for i in range(1, n + 1):
                res.append([i])
            return res

        def dfs(path, num, total, count):
            if num == 2:
                for i in range(count, total):
                    for j in range(i + 1, total):
                        res.append(path + [i, j])
                return

            for i in range(count, total + 1 - num):
                path.append(i)
                dfs(path, num - 1, total, i + 1)
                path.pop()

        dfs([], k, n + 1, 1)

        return res


n = 1
k = 1

s = Solution()
print(s.combine(n, k))
