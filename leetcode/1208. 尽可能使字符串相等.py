class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        a = []
        for i in range(len(s)):
            a.append(abs(ord(s[i]) - ord(t[i])))
        max_length = 0
        a_sum = 0
        pro = 0
        pre = 0
        while pro < len(a):
            if a_sum + a[pro] <= maxCost:
                a_sum += a[pro]
                pro += 1
            else:
                max_length = max(max_length, pro - pre)
                if pre < pro:
                    a_sum -= a[pre]
                    pre += 1
                else:
                    pre += 1
                    pro = pre
                    a_sum = 0

        return max(max_length, pro - pre)


s = "krpgjbjjznpzdfy"
t = "nxargkbydxmsgby"
cost = 14
so = Solution()
print(so.equalSubstring(s, t, cost))
