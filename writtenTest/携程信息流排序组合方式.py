import math

n_htl, n_poi, n_vac = [int(i) for i in input().split(",")]

total = n_htl + n_poi + n_vac

res = [0, True]

dp = [(0, 1), (-1, 0), (0, -1)]


def dfs(l_list, h, p, v, x, y):
    if h == p == v == 0:
        res[0] += 1
        return


    if y == 0:
        num_tem1 = [1, 2, 3]
        num_tem1.remove(l_list[x - 1][y])
        for i in num_tem1:
            if i == 1 and h >0:
                l_list[x][y] = i
                h -= 1
                dfs(l_list, h, p, v, x, y + 1)
            elif i == 2 and p > 0:
                l_list[x][y] = i
                p -= 1
                dfs(l_list, h, p, v, x, y + 1)
            elif i == 3 and v > 0:
                l_list[x][y] = i
                v -= 1
                dfs(l_list, h, p, v, x, y + 1)

    else:
        num_tem2 = [1, 2, 3]
        if y > 0 and l_list[x][y - 1] in num_tem2:
            num_tem2.remove(l_list[x][y - 1])
        if x > 0 and l_list[x - 1][y] in num_tem2:
            num_tem2.remove(l_list[x - 1][y])
        for i in num_tem2:
            if i == 1 and h > 0:
                l_list[x][y] = i
                h -= 1
                dfs(l_list, h, p, v, x + 1, 0)
            elif i == 2 and p > 0:
                l_list[x][y] = i
                p -= 1
                dfs(l_list, h, p, v, x + 1, 0)
            elif i == 3 and v > 0:
                l_list[x][y] = i
                v -= 1
                dfs(l_list, h, p, v, x + 1, 0)



for i in range(1, 4):
    layout = [[0, 0] for _ in range(math.ceil(total // 2))]
    layout[0][0] = i
    if i == 1:
        dfs(layout, n_htl - 1, n_poi, n_vac, 0, 1)
    elif i == 2:
        dfs(layout, n_htl, n_poi - 1, n_vac, 0, 1)
    else:
        dfs(layout, n_htl, n_poi, n_vac - 1, 0, 1)

print(res[0])
