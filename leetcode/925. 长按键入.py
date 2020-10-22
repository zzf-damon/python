class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        pre = 0
        pro = 0
        while pro < len(typed):
            if pre < len(name) and name[pre] == typed[pro]:
                pre += 1
                pro += 1
            elif pro > 0 and typed[pro] == typed[pro-1]:
                pro += 1
            else:
                return False
    
        return pre == len(name)

name = "zlexya"
typed = "aazlllllllllllllleexxxxxxxxxxxxxxxya"

s = Solution()
print(s.isLongPressedName(name,typed))



