def solution(m):
    if len(m) < 2:
        if m != "Z":
            return 2
        else:
            return 1

    res = [m]
    if m[0] != 'Z' and m[1] != "A":
        res.append(chr(ord(m[0]) + 1) + chr(ord(m[1]) - 1) + m[2:])

    i = 1
    while i < len(m) - 1:
        if m[i] != 'Z' and m[i - 1] != "A":
            tem = m[:i] + chr(ord(m[i - 1]) + 1) + chr(ord(m[i]) - 1) + m[i + 2:]
            res.append(tem)
        if m[i] != 'Z' and m[i + 1] != "A":
            tem = m[:i] + chr(ord(m[i]) + 1) + chr(ord(m[i + 1]) - 1) + m[i + 2:]
            res.append(tem)
        i += 1
    if m[-2] != 'A' and m[-1] != "Z":
        res.append(m[:-2] + chr(ord(m[-2]) - 1) + chr(ord(m[-1]) + 1))

    return len(set(res))


list1 = []
while True:
    n = input()
    if n == "":
        break
    m = input()
    list1.append((n, m))

for i in list1:
    print(solution(i[1]))
