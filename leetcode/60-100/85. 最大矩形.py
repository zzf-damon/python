from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        if len(matrix) < 1: return res
        h = len(matrix)
        w = len(matrix[0])

        def dfs(y, x):
            stack_h = [y]
            stack_w = [x]
            max_m = 1
            for i in range(x + 1, w):
                if matrix[y][i] == "1":
                    stack_w.append(i)
                else:
                    break
            for i in range(y + 1, h):
                j = x
                if matrix[i][j] == "1":
                    stack_h.append(i)
                    j += 1
                else:
                    break
                while (j - x) < len(stack_w):
                    if matrix[i][j] != "1":
                        max_m = max(max_m, (i - y) * (stack_w[-1] - x + 1))
                        stack_w = stack_w[:(j - x)]
                    j += 1
            return max(max_m, len(stack_h) * len(stack_w))

        for i in range(h):
            for j in range(w):
                if matrix[i][j] != "0":
                    res = max(res, dfs(i, j))
        return res


# matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# matrix =[["0","0"]]
matrix = [["1", "0", "1", "1", "1"], ["0", "1", "0", "1", "0"], ["1", "1", "0", "1", "1"], ["1", "1", "0", "1", "1"],
          ["0", "1", "1", "1", "1"]]
s = Solution()
print(s.maximalRectangle(matrix))


class Solution1:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        # 记录当前位置上方连续“1”的个数
        pre = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n):
                # 前缀和
                pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0

            # 单调栈
            stack = [-1]
            for k, num in enumerate(pre):
                while stack and pre[stack[-1]] > num:
                    index = stack.pop()
                    res = max(res, pre[index] * (k - stack[-1] - 1))
                stack.append(k)

        return res
s1 = Solution1()
print(s1.maximalRectangle(matrix))