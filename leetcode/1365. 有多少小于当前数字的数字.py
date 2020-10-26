'''
Author: zzf
Date: 2020-10-26 11:56:16
LastEditors: zzf
LastEditTime: 2020-10-26 11:57:14
Description: python script
'''


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        def quickSort(listx):
            if len(listx) <= 1:
                return listx
            pivot = listx[len(listx) // 2]  # 取列表中中间的元素为被比较数pivot
            listl = [x for x in listx if x < pivot]  # <pivot的放在一个列表
            listm = [x for x in listx if x == pivot]  # =pivot的放在一个列表
            listr = [x for x in listx if x > pivot]  # >pivot的放在一个列表
            left = quickSort(listl)  # 递归进行该函数
            right = quickSort(listr)  # 递归进行该函数
            return left + listm + right  # 整合

        nums = quickSort(nums)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, -1, -1):
                if j < i:
                    res.append(j)
                    break
        print(res)
        return res

nums = [8, 1, 2, 2, 3]
s = Solution()
s.smallerNumbersThanCurrent(nums)
