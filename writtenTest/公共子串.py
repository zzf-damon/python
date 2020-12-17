class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        ans = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                # print(dp)
        print(ans)
        return ans


s = Solution()

a = "asdfasdf"
b = "asdffasdf"
s.longestCommonSubsequence(a, b)


def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'

    res = [""]

    def get_res(flag, a, x, y):
        if x == 0 or y == 0:
            return
        if flag[x][y] == 'ok':
            get_res(flag, a, x - 1, y - 1)
            res[0] += a[x - 1]
        elif flag[x][y] == 'left':
            get_res(flag, a, x, y - 1)
        else:
            get_res(flag, a, x - 1, y)

    get_res(flag, a, lena, lenb)

    return res[0]


# a = ""
# b = ""
a = "1A2C3D4B56"
b = "B1D23CA45B6A"
flag = lcs(a, b)
print(flag)

pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 8, 6]


class Node():
    def __init__(self, x):
        self.v = x
        self.left = None
        self.right = None


def main(p: list, t: list) -> list:
    def getTree(pre, tin):
        if not pre:
            return None
        root = Node(pre[0])
        root_index = tin.index(pre[0])
        root.left = getTree(pre[1:1 + root_index], tin[:root_index])
        root.right = getTree(pre[1 + root_index:], tin[root_index + 1:])
        return root

    tree = getTree(p, t)
    res = []

    def postTravel(root):
        if not root:
            return None
        postTravel(root.left)
        postTravel(root.right)
        res.append(root.v)

    postTravel(tree)
    return res


print(main(pre, tin))


s1='abcdefgaa'
s2='defgabc'

def findcom(str1,str2):
    xmax=0 # 记录最大的值,即最大的字串长度
    xindex=0 # 记录最大值的索引位置

    matrix=[]

    for y,yitem in enumerate(str2):
        matrix.append([]) # 每次对str2迭代,生成新的子列表保存比对结果
        for x,xitem in enumerate(str1):
            if xitem != yitem:
                matrix[y].append(0) # 矩阵比较中,元素不同,置矩阵元素为0
            else:
                if x==0 or y==0: # 对处于矩阵第一行,第一列的直接置1,防止索引超界
                    matrix[y].append(1)
                else:
                    matrix[y].append(matrix[y-1][x-1]+1) # 左上角的值+1

                if matrix[y][x] > xmax: # 此轮中最大的字串长度超过记录值
                    xmax=matrix[y][x]
                    xindex=x # 最大值的索引位置

    return str1[xindex+1-xmax:xindex+1] # xindex+1因为后开特性,xindex+1后需往前回溯3个位置

print(findcom(a,b))



def intersect(a, b):
    nums1 = [i for i in a]
    nums2 = [i for i in b]
    nums1.sort()
    nums2.sort()

    length1, length2 = len(nums1), len(nums2)
    intersection = list()
    index1 = index2 = 0
    while index1 < length1 and index2 < length2:
        if nums1[index1] < nums2[index2]:
            index1 += 1
        elif nums1[index1] > nums2[index2]:
            index2 += 1
        else:
            intersection.append(nums1[index1])
            index1 += 1
            index2 += 1

    return "".join(intersection)

print(intersect(a,b))

# coding:utf-8
'''
求两个字符串的最长公共子串
思想：建立一个二维数组，保存连续位相同与否的状态
'''


def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    return str1[p - maxNum:p], maxNum




def find_lcseque(s1, s2):
    m = [ [ 0 for x in range(len(s2)+1) ] for y in range(len(s1)+1) ]
    d = [ [ None for x in range(len(s2)+1) ] for y in range(len(s1)+1) ]
    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                m[p1+1][p2+1] = m[p1][p2]+1
                d[p1+1][p2+1] = 'ok'
            elif m[p1+1][p2] > m[p1][p2+1]:
                m[p1+1][p2+1] = m[p1+1][p2]
                d[p1+1][p2+1] = 'left'
            else:
                m[p1+1][p2+1] = m[p1][p2+1]
                d[p1+1][p2+1] = 'up'
    (p1, p2) = (len(s1), len(s2))
    s = []
    while m[p1][p2]:
        c = d[p1][p2]
        if c == 'ok':
            s.append(s1[p1-1])
            p1-=1
            p2-=1
        if c =='left':
            p2 -= 1
        if c == 'up':
            p1 -= 1
    s.reverse()
    return ''.join(s)

a = "1A2C3D4B56"
b = "B1D23CA45B6A"
res = find_lcseque(a, b)
print(res)


