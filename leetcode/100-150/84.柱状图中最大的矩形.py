from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        area = 0
        if length < 1: return area
        stack = []
        top_len = 0
        i = 0
        while i < length:
            if not stack or i == length - 1 or heights[i] >= heights[stack[-1]]:
                top_len = heights[i]
                stack.append(i)
                i += 1

            while (i == length or top_len > heights[i]) and stack:
                top_len = heights[stack.pop()]
                c = i - (stack[-1] if stack else 0) - 1 if stack else i
                area = max(area, top_len * c)
                top_len = heights[stack[-1]] if stack else 0
        return area


# a = [2, 1, 5, 5, 6, 2, 3]
# a = [1, 1]
a = [2]
# a = [2, 4]
s = Solution()
print(s.largestRectangleArea(a))


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
