from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]



nums = [1, 1, 1, 2, 2, 3]
k = 2


s = Solution()
print(s.topKFrequent(nums, k))
