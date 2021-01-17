from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: return True
        x1, y1 = coordinates[0]
        for i in range(len(coordinates)):
            coordinates[i] = [coordinates[i][0] - x1, coordinates[i][1] - y1]
        k, b = coordinates[1]
        for x, y in coordinates[2:]:
            if b * x - k * y != 0:
                return False

        return True


coordinates = [[0,0],[0,1],[0,-1]]
s = Solution()
print(s.checkStraightLine(coordinates))
