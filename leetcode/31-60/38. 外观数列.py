# fixme 68 ms	13.5 MB



def countAndSay(n):
    if n == 1: return "1"
    sign = "1"
    for i in range(1, n):
        tem = ""
        pre = 0
        number = sign[0]
        count = 0
        while pre < len(sign):
            if sign[pre] == number:
                count += 1
            else:
                tem += str(count) + str(number)
                count = 1
                number = sign[pre]
            if pre == len(sign) - 1:
                tem += str(count) + str(sign[pre])
            pre += 1
        sign = tem
    return sign


countAndSay(7)
