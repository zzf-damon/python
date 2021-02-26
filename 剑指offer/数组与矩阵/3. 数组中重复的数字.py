# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        b = set()
        for i in numbers:
            if i not in b:
                b.add(i)
            else:
                duplication[0] = i
                return True

        return False


a = [6, 3, 2, 0, 2, 5, 0]
b = [-1]
s = Solution()
print(s.duplicate(a, b))
