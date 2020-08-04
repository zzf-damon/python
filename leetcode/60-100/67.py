dungeon = [[100]]


def calculateMinimumHP(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])
    dungeon[m - 1][n - 1] = min(0, dungeon[m - 1][n - 1])

    for i in range(m - 2, -1, -1):
        dungeon[i][-1] = min(0, (dungeon[i + 1][-1] + dungeon[i][-1]))

    for j in range(n - 2, -1, -1):
        dungeon[-1][j] = min(0, (dungeon[-1][j + 1] + dungeon[-1][j]))

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dungeon[i][j] = min(0, dungeon[i][j] +
                                max(dungeon[i + 1][j], dungeon[i][j + 1]))

    return 1 - dungeon[0][0]


print(calculateMinimumHP(dungeon))
