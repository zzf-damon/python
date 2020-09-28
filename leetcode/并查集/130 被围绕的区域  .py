from typing import List

re = [["X", "O", "X", "O", "X", "O"], ["O", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "O"],
      ["O", "X", "O", "X", "O", "X"]]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        used = set()

        fx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if board[i][j] == "O":
                for tem_x, tem_y in fx:
                    new_x, new_y = tem_x + i, tem_y + j
                    if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in used:
                        used.add((new_x, new_y))
                        dfs(new_x, new_y)
            else:
                return

        for i in range(n):
            for j in range(m):
                if 0 < i < n - 1:
                    if (j == 0 or j == m - 1) and (i, j) not in used:
                        used.add((i, j))
                        dfs(i, j)
                else:
                    used.add((i, j))
                    dfs(i, j)

        for i in range(n):
            for j in range(m):
                if (i, j) not in used:
                    # print(i,j)
                    board[i][j] = "X"

        print(board)



a = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
     ["O", "X", "O", "X", "O", "X"]]

s = Solution()
s.solve(a)
