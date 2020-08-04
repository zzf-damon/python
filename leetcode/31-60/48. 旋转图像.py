from pprint import pprint
from typing import List

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
matrix3 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]


# theme 不能新建数组求解

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def backtrack(matrix1, row, col):
            length = len(matrix1) - 1 - row - col
            for i in range(length):
                if row == col:
                    matrix1[row][col], matrix1[col][row + length], matrix1[row + length][col + length], \
                    matrix1[row + length][
                        row] = matrix1[row + length][row], matrix1[row][col], matrix1[col][row + length], \
                               matrix1[row + length][
                                   col + length]
                else:
                    matrix1[row][col], matrix1[col][row + length], matrix1[row + length][length - col], \
                    matrix1[length - col][
                        row] = matrix1[length - col][row], matrix1[row][col], matrix1[col][row + length], \
                               matrix1[row + length][
                                   length - col]
                col += 1
            if length > 2:
                backtrack(matrix1, row + 1, row + 1)

        backtrack(matrix, 0, 0)


def backtrack(matrix1, row, col):
    length = len(matrix1) - 1 - row - col
    for i in range(length):
        if row == col or row != 0:
            print(matrix1[row][col])
            print(matrix1[col][row + length])
            print(matrix1[row + length][length + row])
            print(matrix1[length + row][row])
            # matrix1[row][col], matrix1[col][row + length], matrix1[row + length][col + length], matrix1[row + length][
            #     row] = matrix1[row + length][row], matrix1[row][col], matrix1[col][row + length], matrix1[row + length][
            #     col + length]
        else:
            print(matrix1[row][col])
            print(matrix1[col][row + length])
            print(matrix1[row + length][length - col])
            print(matrix1[length - col][row])
            # matrix1[row][col], matrix1[col][row + length], matrix1[row + length][length - col], matrix1[length - col][
            #     row] = matrix1[length - col][row], matrix1[row][col], matrix1[col][row + length], matrix1[row + length][
            #     length - col]
        col += 1
    if length > 2:
        backtrack(matrix1, row + 1, row + 1)
    # elif length == 2:
    #     print(matrix1[row + 1][row + 1])
    else:
        return


backtrack(matrix3, 0, 0)
pprint(matrix3)


# 旋转四个矩阵
class Solution1:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate 4 elements
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row


# 转置加翻转 最基本的思路
class Solution2:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

                # reverse each row
        for i in range(n):
            matrix[i].reverse()
