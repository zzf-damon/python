from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        tem_list = Counter(S)
        count = 0
        for i in J:
            if i in tem_list:
                count += tem_list[i]

        print(count)
        return count


s = Solution()
J = "aA"
S = "aAAbbbb"
s.numJewelsInStones(J, S)
