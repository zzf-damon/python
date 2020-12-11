def s(A, B):
    m = len(A)
    n = len(B)
    for i in range(n):
        A.append(-1)
    pa, pb = m - 1, 0
    tail = m + n - 1
    while pa >= 0 or pb < n:
        if pa == -1:
            A[tail] = B[pb]
            pb += 1
        elif pb == n:
            A[tail] = A[pa]
            pa -= 1
        elif A[pa] > B[pb]:
            A[tail] = A[pa]
            pa -= 1
        else:
            A[tail] = B[pb]
            pb += 1
        tail -= 1
    return A


# a=[2,3,3,6,7]
# a = [1, 2, 3]
# b=[10,7,5,1]
# b = [4, 5, 6]
a = []
b = [1]
print(s(a, b))

import math


def comb(n, m):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))


for i in range(101):
    r = comb(100, i) * (0.8 ** i) * (0.2 ** (100 - i))
    if r >= 0.8:
        print(i)
