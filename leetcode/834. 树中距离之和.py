from typing import List

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(N)]
        for baba, erza in edges:
            tree[baba].append(erza)
            tree[erza].append(baba)
        depth = [0 for _ in range(N)]
        count = [0 for _ in range(N)]


        def dfsForDepthAndCount(baba0, father):
            count[baba0] = 1
            for erza0 in tree[baba0]:
                if erza0 != father:
                    depth[erza0] = depth[baba0] + 1
                    dfsForDepthAndCount(erza0, baba0)
                    count[baba0] += count[erza0]


        dfsForDepthAndCount(0, -1)
        answer = [0 for _ in range(N)]
        answer[0] = sum(depth)


        def dfsForAnswer(baba1, father):
            for erza1 in tree[baba1]:
                if erza1 != father:
                    answer[erza1] = answer[baba1] + N - 2 * count[erza1]
                    dfsForAnswer(erza1, baba1)


        dfsForAnswer(0, -1)
        return answer