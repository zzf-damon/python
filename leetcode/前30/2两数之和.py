nums = [-1, -2, -3, -4, -5]


class Solution:
    def twoSum(self, nums, target: int):
        for k, i in enumerate(nums):
            # if i > target:
            #     continue
            j = target - i
            pre_list = nums[k + 1:]
            if j in pre_list:
                j_index = pre_list.index(j)
                return [k, j_index + k + 1]


target = -8
solution = Solution()
print(solution.twoSum(nums, target))



from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = 0 
        while nums:
            tem = nums.pop(0)
            if (target- tem) in nums:
                pro = nums.index(target-tem)
                break
            pre += 1
        return [pre,pro+pre+1]


s1 = Solution1()

print(s1.twoSum(nums,target))