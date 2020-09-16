import math
import torch
import torch.nn as nn
import torch.nn.functional as f



class Solution:
    def main(self, number):
        if len(number) < 1: return 0
        res_list = [number]
        length = len(number)

        def dfs(depth, path):
            if depth == length:
                tem = ""
                for i in path:
                    tem += str(i)
                res_list.append(tem)
                return
            total = path[-1] + int(number[depth])
            if total % 2 == 0:
                path.append(int(total/2))
                dfs(depth+1,path)
            else:
                path1 = path.copy()
                path.append(math.ceil(total/2))
                dfs(depth+1,path)

                path1.append(math.floor(total/2))
                dfs(depth+1,path1)



        for i in range(10):
            dfs(1, [i])

        return len(set(res_list)) -1


     


n = "123"
n1 = "12345"
n2 = "09"
n3 = "3"

a = Solution()
print(a.main(n))
print(a.main(n1))
print(a.main(n2))
print(a.main(n3))

