def solution(n, m, k, list_total):
    dict1 = {}
    for i in list_total:
        dict_tem = {
            "key": i[1],
            "value": i[2]
        }
        if i[0] not in dict1.keys():
            dict1[i[0]] = [dict_tem]
        else:
            dict1[i[0]] += [dict_tem]

    res = []

    def dfs(used, m, node, path, dict1):
        if len(path) == m and False not in used:
            res.append(path[:])
            return
        if node in dict1.keys():
            for i in dict1[node]:
                if i["value"] <= k:
                    path.append(i["key"])
                    used[i["key"] - 1] = True
                    dfs(used, m, i["key"], path, dict1)
                    used[i["key"] - 1] = False
                    path.pop()
        else:
            return

    for i in list(dict1.keys()):
        used = [False] * m
        used[0] = True
        dfs(used, m, i, [i], dict1)
        if res:
            return True

    return False


# T = int(input())
#
# pre = 0
# while pre < T:
#     pre += 1
#     n, m, k = [int(i) for i in input().split(" ")]
#     list_tem = []
#     for i in range(int(m)):
#         tem = [int(i) for i in input().split(" ")]
#         list_tem.append(tem)
#
#     print(solution(n, m, k, list_tem))


n, m, k = 3, 3, 400
list1 = [
    [1, 2, 200],
    [1, 3, 300],
    [2, 3, 500]]

list2 = [
    [1, 2, 500],
    [1, 3, 600],
    [2, 3, 700]]

print(solution(n, m, k, list1))
