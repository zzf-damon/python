n, m = map(int, input().split())
dp = [0] * (m + 1)
for i in range(1, n + 1):
    num, v, w = map(int, input().split())
    for j in range(v, m + 1):
        dp[j] = max(dp[j], dp[j - v] + w)
print(dp[m])