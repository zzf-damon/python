from typing import List
import collections

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = collections.Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    print(-u - v)
                    ans += countAB[-u - v]
                    print(countAB)
        return ans


A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]

s = Solution()
print(s.fourSumCount(A, B, C, D))
