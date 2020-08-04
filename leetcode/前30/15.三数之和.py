from pprint import pprint

list_a = [-1, 0, 1, 2, -1, -4]


def threeSum(nums):
    List_ = []
    for i, i_num in enumerate(nums):
        for j, j_num in enumerate(nums[i + 1:]):
            for k_num in nums[i + j + 2:]:
                if k_num + i_num + j_num == 0:
                    list_b = [i_num, j_num, k_num]
                    list_b.sort()
                    if list_b not in List_:
                        List_.append(list_b)
    pprint(List_)
    return List_


threeSum(list_a)


class Solution:
    def threeSum(self, nums):

        n = len(nums)
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res


sou = Solution()

sou.threeSum(list_a)
