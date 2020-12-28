from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        sell = [i for i in range(n)]
        mono_stack = list()
        for i in range(n):
            if mono_stack and prices[i] >= prices[mono_stack[-1]]:
                sell[mono_stack[0]] = i
                mono_stack.append(i)
            else:
                mono_stack = list()
                mono_stack.append(i)
        res = [prices[sell[i]] - prices[i] for i in range(n) if i != sell[i]]
        return sum(sorted(res)[-k:])


k = 2
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]

# k = 2
# prices = [6, 1, 3, 2, 4, 7]
s = Solution()
print(s.maxProfit(k, prices))




def maxProfit(k: int, prices: List[int]) -> int:
    if not prices:
        return 0

    n = len(prices)
    k = min(k, n // 2)
    buy = [0] * (k + 1)
    sell = [0] * (k + 1)

    buy[0], sell[0] = -prices[0], 0
    for i in range(1, k + 1):
        buy[i] = sell[i] = float("-inf")

    for i in range(1, n):
        buy[0] = max(buy[0], sell[0] - prices[i])
        for j in range(1, k + 1):
            buy[j] = max(buy[j], sell[j] - prices[i])
            sell[j] = max(sell[j], buy[j - 1] + prices[i])

    return max(sell)


print(maxProfit(k,prices))




def maxProfit1(k: int, prices: List[int]) -> int:
    if not prices:
        return 0

    n = len(prices)
    k = min(k, n // 2)
    buy = [[0] * (k + 1) for _ in range(n)]
    sell = [[0] * (k + 1) for _ in range(n)]

    buy[0][0], sell[0][0] = -prices[0], 0
    for i in range(1, k + 1):
        buy[0][i] = sell[0][i] = float("-inf")

    for i in range(1, n):
        buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
        for j in range(1, k + 1):
            buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
            sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])

    return max(sell[n - 1])
print(maxProfit1(k,prices))