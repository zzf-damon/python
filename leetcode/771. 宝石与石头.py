from collections import Counter

import requests

url = "https://www.baidu.com/?tn=02003390_hao_pg"
response = requests.get(url)
print(response.text)
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
