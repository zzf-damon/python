T = int(input())

for _ in range(T):
    n, m = [int(i) for i in input().split(" ")]
    list_tem = []
    start = (0, 0)
    end = (0, 0)
    for i in range(n):
        list_1 = input()
        for j, key in enumerate(list_1):
            if key == "S":
                start = (i, j)
            if key == "E":
                end = (i, j)

        list_tem.append(list_1)

    if start == end:
        print("Yes")

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    used = set()


    def dfs(subscript):
        if subscript == end: return True
        used.add(subscript)
        result = False
        for i in direction:
            new_x, new_y = i[0] + subscript[0], i[1] + subscript[1]
            if 0 <= new_x < n and 0 <= new_y < m:
                if (new_x, new_y) not in used and list_tem[new_x][new_y] != "#":
                    if dfs((new_x, new_y)):
                        result = True
                        break
        used.remove(subscript)
        return result


    if dfs(start):
        print("YES")
    else:
        print("NO")
