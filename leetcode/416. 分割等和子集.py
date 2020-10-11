from typing import List
from collections import Counter


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pre = 0
        pro = len(nums) - 1
        nums = sorted(nums)
        tem = 0
        while pre < pro:
            if tem <= 0:
                tem = nums[pro] + tem - nums[pre]
            else:
                tem -= nums[pre]
            if tem == 0 and pro - pre == 1:
                return True
            if tem <= 0:
                pro -= 1
            pre += 1
        return False


# data = [1, 5, 11, 5]
data = [2, 2, 1, 1]
s = Solution()
print(s.canPartition(data))


class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target] == 1


s1 = Solution1()
print(s1.canPartition(data))


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]


s2 = Solution2()
print(s2.canPartition(data))
