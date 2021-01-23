import collections
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1

        edge = collections.defaultdict(list)
        rec = collections.defaultdict(list)

        for i, (x, y) in enumerate(connections):
            rec[x].append(i)
            rec[y + 100001].append(i)

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


n = 4
connections = [[0, 1], [0, 2], [1, 2]]
s = Solution()
s.makeConnected(n, connections)
