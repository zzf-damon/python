from collections import Counter

class Solution:
    def minimumOperations(self, leaves: str) -> int:

        dict_tem = Counter(leaves)
        count = 0
        signA = True
        for  i in leaves:
            if i == "r" and signA == True:


leaves = "rrryyyrryyyrr"
s = Solution()
s.minimumOperations(leaves)
