nums_1 = [-1, 2, 1, -4]
nums_2 = [1, -1, 3, -3]
target = 1


# 484 ms	13.4 MB
def threeSumClosest(nums, target):
    res = 0x7fffffff
    nums.sort()
    # compare_size = lambda x, y: x + 1 if x > y else y + 1
    for i, num in enumerate(nums):
        L = i + 1
        R = len(nums) - 1
        while R > L:
            total = num + nums[L] + nums[R]
            res = total if abs(total - target) <= abs(res - target) else res
            if R - 1 == L: break
            while R > L and R - 1 != L:
                if total > target:
                    R -= 1
                    if nums[R] < nums[R + 1]: break
                else:
                    L += 1
                    if nums[L] > nums[L - 1]: break
    return res


threeSumClosest(nums=nums_2, target=target)


# 36 ms	13.4 MB
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums = sorted(nums)
        # 和目标值相差的值，计算绝对值
        closestNum: int = nums[0] + nums[1] + nums[2]
        i: int = 0
        while i < len(nums) - 2:
            left: int = i + 1
            right: int = len(nums) - 1
            while left < right:
                # 判断最小值
                minNum: int = nums[i] + nums[left] + nums[left + 1]
                if target < minNum:
                    if abs(closestNum - target) > abs(minNum - target):
                        closestNum = minNum
                    break
                # 判断最大值
                maxNum: int = nums[i] + nums[right] + nums[right - 1]
                if target > maxNum:
                    if abs(closestNum - target) > abs(maxNum - target):
                        closestNum = maxNum
                    break

                tempSum: int = nums[i] + nums[left] + nums[right]
                if tempSum == target:
                    # 居然和target相等，那就是答案
                    return tempSum
                if abs(tempSum - target) < abs(closestNum - target):
                    # 居然找到更小的了，那就更新结果
                    closestNum = tempSum

                if tempSum > target:
                    # 那就把右端朝左移动一位
                    right -= 1
                    # 解决nums[right]重复
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1
                else:
                    # 那就把左端朝右移动一位
                    left += 1
                    # 解决nums[left]重复
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1

            # 解决nums[i]重复
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        print(closestNum)
        return closestNum


solution = Solution()

solution.threeSumClosest(nums_1, target)
