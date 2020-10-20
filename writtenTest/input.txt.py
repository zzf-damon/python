f = open("./input.txt")

dict1 = {}

for i in range(1000):
    dict1[i] = 0

for i in f.readlines():
    number = int(i.strip("\n"))
    mod = number // 100
    if mod in dict1.keys():
        dict1[mod] += 1

for i in dict1:
    if i == 0:
        print("0-99 %d" % dict1[i])
    else:
        print("%d00-%d99 %d" % (i, i, dict1[i]))

import json
content = input()
label = json.loads(input())
keywords = []
string = []
pre = 0
tem_k = ""
tem_s = ""
signA = True
while pre < len(content):
    if label[pre] == 0 and signA:
        pre += 1
        continue
    if label[pre] == 1 or label[pre] == 2:
        tem_k += content[pre]
        signA = False
    if label[pre] == 3 or label[pre] == 4:
        tem_s += content[pre]
        signA = False
    if not signA and (label[pre] == 0 or pre == len(label) -1):
        if tem_k:
            keywords.append(tem_k)
            tem_k = ""
            signA = True
        if tem_s:
            string.append(tem_s)
            tem_s = ""
            signA = True
    pre += 1

print(keywords)
print(string)




# content = "想知道如果提高王者荣耀水平，上分把妹不是梦，加微信：17252sugats78,加QQ:34676328889。"
# label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
#          4, 4, 0, 0, 1, 2, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,0]