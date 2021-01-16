
from typing import List
import collections



class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        edge = collections.defaultdict(list)
        rec = collections.defaultdict(list)
        for i, (x, y) in enumerate(stones):
            rec[x].append(i)
            rec[y + 10001].append(i)

        for vec in rec.values():
            k = len(vec)
            for i in range(1, k):
                edge[vec[i - 1]].append(vec[i])
                edge[vec[i]].append(vec[i - 1])

        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)

        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)

        return n - num


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
# stones = [[0, 0]]
s = Solution()
print(s.removeStones(stones))
