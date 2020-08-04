def test(s):
    if len(s) == 1:
        return 0
    used = []
    for i, j in enumerate(s):
        tem_1 = None
        tem_2 = None
        pre = 0
        pro = len(s) - 1
        while pre < i:
            if s[pre] == j:
                tem_1 = pre
                break
            pre += 1
        while pro > i:
            if s[pro] == j:
                tem_2 = pro
                break
            pro -= 1
        if tem_1 != None and tem_2 != None:
            continue
        elif tem_1 != None and not tem_2:
            used.append(tem_1)
        elif tem_2 != None and not tem_1:
            used.append(tem_2)
    print(used)
    res = [0] * len(used)
    pre = 1
    while pre < len(used):
        if used[pre] < used[pre -1]:
            res[pre] = res[pre - 1] + 1
        else:
            res[pre] = res[pre - 1] - 1
        pre += 1
    print(res)
    return max(res) + 1


s = "ldbslscbl"

print(test(s))
