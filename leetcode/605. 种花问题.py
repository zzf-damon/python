from typing import List
import math


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if n > (math.ceil(len(flowerbed) / 2) - sum(flowerbed)): return False
        i = 0
        length = len(flowerbed)
        total = sum(flowerbed)
        while i < len(flowerbed) and n > 0:
            if n > (math.ceil(length / 2) - total): return False
            if flowerbed[i] == 0:
                length -= 1 if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1 else 0
                if n > (math.ceil(length / 2) - total): return False
                n -= 1
            else:
                total -= 1
            i += 2
            length -= 2
        return True


# flowerbed = [0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]
flowerbed = [0,1,0]
n = 1
s = Solution()
print(s.canPlaceFlowers(flowerbed, 1))
