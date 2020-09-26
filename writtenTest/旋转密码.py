def transpose(matrix):
    n = len(matrix[0])
    rem = []
    matrix_tem = []
    for i in range(n):
        for k, key in enumerate(matrix[i]):
            if key == "0":
                rem.append((i, k))
        matrix_tem.append([j for j in matrix[i]])

    for i in range(n):
        for j in range(i, n):
            matrix_tem[j][i], matrix_tem[i][j] = matrix_tem[i][j], matrix_tem[j][i]

    for i in range(n):
        matrix_tem[i].reverse()

    return matrix_tem, rem


class Solution:
    def rotatePassword(self, s1, s2):
        res_list = []
        for _ in range(4):
            s1, rem = transpose(s1)
            res_list += rem
        res_str = ""

        for j, k in res_list:
            res_str += s2[j][k]

        return res_str


s1 = ["1101", "1010", "1111", "1110"]
s2 = ["ABCD", "EFGH", "IJKL", "MNPQ"]

S = Solution()
print(S.rotatePassword(s1, s2))
