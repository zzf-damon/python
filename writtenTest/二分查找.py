def solution(tem_list, number):
    if number == 0: return 0
    tem_list = tem_list[number:] + list(reversed(tem_list[:number]))
    left, right = 0, len(tem_list) - 1
    while left <= right:
        p = left + (right - left) // 2
        if tem_list[p] == number:
            return (p + number) % len(tem_list) - 1
        if number < tem_list[p]:
            right = p - 1
        else:
            left = p + 1
    return -1


A = [5, 0, 1, 2, 3, 4]
target = 1
print(solution(A, target))
