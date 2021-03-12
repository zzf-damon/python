class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for pre in S:
            if stack and pre == stack[-1]:
                stack.pop()
            else:
                stack.append(pre)
        return "".join(stack)


a = "abbaca"
s = Solution()
print(s.removeDuplicates(a))
