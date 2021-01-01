from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        a = []
        b = []
        i = 0
        while i < len(intervals):
            if not a:
                a.append(intervals[i][0])
                b.append(intervals[i][1])
            elif intervals[i][0] >= b[-1]:
                a.append(intervals[i][0])
                b.append(intervals[i][1])
            elif intervals[i][0] == a[-1] and intervals[i][1] <= b[-1]:
                b[-1] = intervals[i][1]
            i += 1

        return len(intervals) - len(a)


a = [[1, 2], [2, 3], [3, 4], [1, 3]]
b = [[2, 4], [3, 5], [1, 3]]
c = [[1, 100], [11, 22], [1, 11], [2, 12]]
s = Solution()
# print(s.eraseOverlapIntervals(a))
# print(s.eraseOverlapIntervals(b))
print(s.eraseOverlapIntervals(c))
