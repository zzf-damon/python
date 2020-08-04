list1 = [("ltSb6tmS", 18),
         ("KljAUbN6", 19),
         ("K6j2HAlb", 1),
         ("jj8fPrjS", 17),
         ("TmDhqqo3", 16)]
list2 = []
for i in list1:
    sum1 = 0
    for j in i[0]:
        sum1 += ord(j)
    list2.append(sum1)

print(list2)
