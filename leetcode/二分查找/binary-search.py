from typing import List

# 递归
# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:
        mid = int(l + (r - l) / 2)
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # 不存在
        return -1

# 不递归
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1
