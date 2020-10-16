a = int(input())

for i in range(a, 10 ** 7):
    if i <= 10:
        print(i)
        break
    tem = str(i)[0]
    signB = True
    for j in range(1, len(str(i))):
        if tem < str(i)[j]:
            signB = False
            break
        tem = str(i)[j]
    if signB:


        print(i)
        break
