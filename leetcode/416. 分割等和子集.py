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
data = [2,2,1,1]
s = Solution()
print(s.canPartition(data))

a = Counter(data)
list_tem = []
for i in a:
    if a[i] % 2 != 0:
        list_tem.append(i)


