def solution(n, k):  # 整数分解
    res = [1]
    if k == 1: return res[0]

    def count(path, index):
        if sum(path) == n:
            res[0] += 1
        for i in range(index, n):
            if len(path) < k and i not in path:
                path.append(i)
                count(path, i)
                path.pop(-1)

    count([], 1)
    return res[0]


n = int(input())
k = int(input())
print(solution(n, k))
