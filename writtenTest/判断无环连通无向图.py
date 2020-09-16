list_test = [3, 6, [9, 12], [2, 11], [1, 3], [6, 10], [5, 7], [4, 8], 5, [1, 3], [2, 4], [5, 9], [6, 8], [7, 10], 5,
             [5, 8], [3, 6], [2, 9], [7, 10], [1, 4]]


def tem_res(used, tem_list):  # 判断是否为无环连通无向图
    res = len(tem_list)
    stack = [tem_list.pop()]
    used += 1
    while stack:
        current = stack.pop()
        if current in tem_list:
            tem_list.remove(current)
        for i in tem_list:
            if current[0] < i[0] < current[1] < i[1] or i[0] < current[0] < i[1] < current[1]:
                stack.append(i)
                used += 1
    return used == res


def solution(list_test):
    number = list_test[0]  # 输入的第一个数
    res = []  # 结果列表                                        
    pre = 1

    for i in range(number):
        tem_list = list_test[pre + 1:pre + list_test[pre] + 1]
        pre = pre + list_test[pre] + 1
        res.append(tem_res(0, tem_list))

    return res


print(solution(list_test))  # 开始


  
# while True:
#     k = input("输入一个数")
