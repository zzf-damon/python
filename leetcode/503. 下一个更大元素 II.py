from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        length = len(nums)
        res = [-1] * length
        for pre in range(2 * length - 1):
            while stack and nums[stack[-1]] < nums[pre % length]:
                res[stack.pop()] = nums[pre % length]
            stack.append(pre % length)
        return res


class Solution1:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()
        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)
        return ret


a = [1, 2, 1]
s = Solution()
print(s.nextGreaterElements(a))
