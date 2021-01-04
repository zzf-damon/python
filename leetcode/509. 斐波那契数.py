# fixme 820 ms	14.8 MB
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        return self.fib(n - 1) + self.fib(n - 2)


# fixme 40 ms	14.6 MB
class Solution1:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        stack = [0, 1]
        res = 0
        for i in range(2, n + 1):
            res = sum(stack)
            stack = [max(stack), res]
        return res


s = Solution()
print(s.fib(7))
s1 = Solution1()
print(s1.fib(7))