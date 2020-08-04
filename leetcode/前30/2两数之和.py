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
                print(i, k, j, j_index + k + 1)
                return [k, j_index + k + 1]


target = -8
solution = Solution()
print(solution.twoSum(nums, target))
