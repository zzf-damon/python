def solution(x):
    count = 0
    while x > 1:
        count += 1
        x = x // 2 if x % 2 == 0 else x * 3 + 1
    return count


number = 10  # 6
print(solution(number))


class Test:
    def solution(self, N, L):
        res = 0

        def dfs(index):
            count = N
            pre = index - 1 if index > 0 else -1
            pro = index + 1 if index < N - 1 else N
            k = pre + 1
            while pre > -1:
                if L[pre] >= L[k]:
                    count -= 1
                else:
                    k = pre
                pre -= 1
            k = pro - 1
            while pro < N:
                if L[pro] >= L[k]:
                    count -= 1
                else:
                    k = pro
                pro += 1
            return count

        for i in range(N):
            res = max(res, dfs(i))

        return res


N = 8
L = [1176, 1176, 1155, 1200, 1160, 1128, 1197, 1220]
s = Test()
print(s.solution(N, L))  # 4
