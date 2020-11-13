str_1 = input()
key = str_1[0]
length = 1
count = 1
res = ""
while length < len(str_1):
    if str_1[length] == key:
        count += 1
        length += 1
    else:
        res += key + str(count)
        key = str_1[length]
        count = 0


print(res + key +str(count))
import torch.nn.functional as F
F.max_pool1d