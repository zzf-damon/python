# n, p, q = [int(i) for i in input().split(" ")]
# a_list = [int(i) for i in input().split(" ")]
# b_list = [int(i) for i in input().split(" ")]
#
# count = 0
# for i in a_list:
#     if i in b_list:
#         count += 1
#
# print(p - count, q - count, count)


# def judge(a_list):
#     while a_list:
#         root = max(a_list)
#         if root != len(a_list) and root != 1 or root == 2:
#             return False
#         a_list.remove(root)
#     return True
#
#
# while True:
#     n = int(input())
#     a_list = [int(i) for i in input().split(" ")]
#     print(judge(a_list))


from collections import Counter

a = [1, 2, 3, 4, 5, 6, 7]
b = [5, 6, 7, 8, 9, 0]

c = a + b

list1 = Counter(c)

list2 = Counter([list1[i] for i in list1])

print(list1)


