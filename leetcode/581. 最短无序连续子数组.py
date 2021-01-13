from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]):
        max_ = max(nums)
        min_ = min(nums)
        l = 0
        r = len(nums) - 1
        for i in range(len(nums)):
            l = i
            if min_ < nums[i]:
                break

        for i in range(r, 0, -1):
            r = i
            if max_ > nums[i]:
                break

        return l, r


nums = [2, 6, 4, 8, 10, 9, 15]

s = Solution()
print(s.findUnsortedSubarray(nums))
