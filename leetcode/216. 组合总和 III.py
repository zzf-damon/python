from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(poor, path, begin):
            if poor == 0 and len(path) == k:
                res.append(path[:])
            for index in range(begin, 10):
                if  poor < index:
                    break
                path.append(index)
                dfs(poor-index, path, index+1)
                path.pop()
        dfs(n, [], 1)
        return res


k = 3
n = 9


s = Solution()
print(s.combinationSum3(k, n))
