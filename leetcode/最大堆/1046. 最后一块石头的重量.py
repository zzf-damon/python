import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 初始化
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        # 模拟
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x - y)

        if heap: return -heap[0]
        return 0


a = [2, 7, 4, 1, 8, 1]
s = Solution()
print(s.lastStoneWeight(a))
