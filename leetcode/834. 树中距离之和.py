from typing import List
from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(N)]
        for baba, erza in edges:
            tree[baba].append(erza)
            tree[erza].append(baba)
        depth = [0 for _ in range(N)]
        count = [0 for _ in range(N)]
        print(depth)













N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
s = Solution()
s.sumOfDistancesInTree(N,edges)