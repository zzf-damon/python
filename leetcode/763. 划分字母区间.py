'''
Author: zzf
Date: 2020-10-22 10:16:15
LastEditors: zzf
LastEditTime: 2020-10-22 10:47:47
Description:763. 划分字母区间
'''

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []

        def dfs(string):
            if len(string) < 1: return
            key = string[0]
            if key not in string[1:]:
                res.append(1)
                dfs(string[1:])
            else:
                index = len(string) - string[::-1].index(key) -1
                tem = index 
                for i in range(index+1, len(string)):
                    if string[i] in string[:tem+1]:
                        tem = i
                res.append(tem+1)
                dfs(string[tem+1:])
        dfs(S)
        return res


s = Solution()
Str = "qiejxqfnqceocmy"


print(s.partitionLabels(Str))




def partitionLabels(S: str) -> List[int]:
    last = [0] * 26
    for i, ch in enumerate(S):
        last[ord(ch) - ord("a")] = i
    
    partition = list()
    start = end = 0
    for i, ch in enumerate(S):
        end = max(end, last[ord(ch) - ord("a")])
        if i == end:
            partition.append(end - start + 1)
            start = end + 1
    
    return partition


partitionLabels(Str)

