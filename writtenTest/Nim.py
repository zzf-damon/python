def solution(s, t, list1):
    path_total = [float("inf"), 0]
    res = [[]]
    dict1 = {}

    for i in list1:
        if i[0] not in dict1.keys():
            dict1[i[0]] = [{"key": i[1], "value": i[2]}]
        else:
            dict1[i[0]] += [{"key": i[1], "value": i[2]}]

    def dfs(path, target, sum):
        if target == t:
            if sum <= path_total[0]:
                res[0] = max(path)
                path_total[0] = sum
                return

        for i in dict1[target]:
            sum += i["value"]
            path.append(i["value"])
            dfs(path, i["key"], sum)
            sum -= i["value"]
            path.pop()

    dfs([s], s, 0)

    return res[0]


n, m, s, t = 5, 6, 1, 5

list1 = [[1, 5, 100],
         [1, 2, 10],
         [2, 5, 5],
         [1, 3, 3],
         [3, 4, 2],
         [4, 5, 1], ]

print(solution(s, t, list1))
