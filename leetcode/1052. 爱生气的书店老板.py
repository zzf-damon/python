from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        minutes = len(customers)
        count = 0
        pre = 0
        pro = X
        temp = 0

        for i in range(minutes):
            if grumpy[i] != 1:
                count += customers[i]
            else:
                count += 0
        
        for i in range(pro):
            if grumpy[i] == 1:
                temp += customers[i]
            else:
                temp += 0
        res = count+temp
        
        while pro < minutes:
            if grumpy[pre] == 1:
                temp -= customers[pre]
            if grumpy[pro] == 1:
                temp += customers[pro]
            res = max(res, count + temp)
            pre += 1
            pro += 1

        return res


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3

s = Solution()
s.maxSatisfied(customers, grumpy, X)
