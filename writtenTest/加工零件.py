from collections import Counter


def solution(list_total, n):
    set1 = Counter(list_total)
    res = 0
    del_list = []
    while set1:
        count = 0
        set1 = set1.most_common()
        for i in set1:
            if set1[i]:
                set1[i] -= 1
                count += 1
                if not set1[i]:
                    del_list.append(i)
            else:
                del_list.append(i)
            if count == n:
                res += n
                break
        for i in del_list:
            del set1[i]
        if count < n:
            res += count if len(set1) < 1 else n

    return res


a = [1, 1, 1, 2, 3, 3, 3, 4, 5, 6, 8, 8, 8]
b = 2
print(solution(a, b + 1))
