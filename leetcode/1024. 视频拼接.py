from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) :
        pre_dict = {}
        pro_dict = {}

        for i in clips:
            if i[0] not in pre_dict.keys():
                pre_dict[i[0]] = i[1]
            else:
                pre_dict[i[0]] = max(pre_dict[i[0]],i[1])
            
            if i[1] not in pro_dict.keys():
                pro_dict[i[1]] = i[0]
            else:
                pro_dict[i[1]] = min(pro_dict[i[1]],i[0])
        
        count = 0
        pre = 0
        pro = T

        while pre < pro:
            pre = pre_dict[i[0]]




        
        tem_list = []
        for i in clips:
            if i[0] == 0:
                pre = max(pre,i[1])
                if pre > pro:
                    return 1
            elif i[1] == T:
                pro = min(pro,i[0])
                if pro < pre:
                    return 1
            else:
                tem_list.append(i)




clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [
    1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]]
T = 9
s = Solution()
s.videoStitching(clips, T)
