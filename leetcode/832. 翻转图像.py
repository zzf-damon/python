from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        length = len(A[0])
        for i in range(len(A)):
            pre = 0
            pro = length - 1
            while pre <= pro:
                if A[i][pre] == A[i][pro] and pre != pro:
                    A[i][pre] = (A[i][pre] + 1) % 2
                    A[i][pro] = (A[i][pro] + 1) % 2
                if pre == pro:
                    A[i][pro] = (A[i][pro] + 1) % 2
                pre += 1
                pro -= 1
        return A


class Solution1:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if A[i][left] == A[i][right]:
                    A[i][left] ^= 1
                    A[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                A[i][left] ^= 1
        return A



# A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

s = Solution()
print(s.flipAndInvertImage(A))
s1 = Solution1()
print(s1.flipAndInvertImage(A))
