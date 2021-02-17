from functools import reduce


class Solution:
    def maxScore(self, cardPoints: [int], k: int) -> int:
        if k >= len(cardPoints): return sum(cardPoints)
        a = cardPoints[:k][::-1] + cardPoints[-k:][::-1]
        sum_a = [a[0]]
        for i in range(1, len(a)):
            sum_a.append(a[i] + sum_a[i - 1])
        pre = 0
        pro = k - 1
        max_res = 0
        while pro < 2 * k:
            sign = sum_a[pro] - sum_a[pre] + a[pre]
            max_res = max(sign, max_res)
            pro += 1
            pre += 1
        return max_res


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
s = Solution()
print(s.maxScore(cardPoints, k))
