list1 = [1, 3, 5, 6]


# 48 ms	14 MB
def searchInsert(nums, target):
    if not nums: return nums
    if target in nums:
        return nums.index(target)
    else:
        pre = 0
        while pre < len(nums):
            if nums[pre] > target:
                return pre
            pre += 1
        return len(nums)


print(searchInsert(list1, target=7))
