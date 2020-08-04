s = "+-+.8"


def isNumber(s: str) -> bool:
    def func(x):
        y = 2 if 48 <= ord(x) <= 57 else -1
        return {
            " ": 0,
            "+": 1,
            "-": 1,
            ".": 3,
            "e": 4
        }.get(x, y)

    list1 = [[0, 1, 6, 2, -1],
             [-1, -1, 6, 2, -1],
             [-1, -1, 3, -1, -1],
             [8, -1, 3, -1, 4],
             [-1, 7, 5, -1, -1],
             [8, -1, 5, -1, -1],
             [8, -1, 6, 3, 4],
             [-1, -1, 5, -1, -1],
             [8, -1, -1, -1, -1]]

    finals = 0b101101000
    state = 0
    for i in s:
        id = func(i)
        if id < 0: return False
        state = list1[state][id]
        if state < 0: return False

    return (finals & (1 << state)) > 0


print(isNumber(s))
