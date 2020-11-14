target = input() # APP依赖
n = int(input())

dict_tem = {}

for i in range(n):
    pre, pro = input().split(" ")
    dict_tem[pre] = [dict_tem.get(pre, pro)]
res = []


def dfs(number, used):
    if number not in dict_tem.keys():
        return
    used.add(number)
    for i in dict_tem[number]:
        if i not in used:
            res.append(i)
            dfs(i, used)


dfs(target, set())
print(len(res))
