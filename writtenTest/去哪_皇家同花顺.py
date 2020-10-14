from collections import Counter

n = int(input())
tem_list = [i for i in input().split(" ")]

list_res = ["HuangJiaTongHuaShun", "TongHuaShun", "SiTiao", "HuLu", "TongHua", "ShunZi", "SanTiao", "LiangDui", "YiDui",
            "GaoPai"]

kapai_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

sign_HuangJiaTongHuaShun = True
sign_tonghuashun = True
sign_sitiao = False
sign_hulu = False
sign_tonghua = True
sign_shunzi = True
sign_santiao = False
sign_liangdui = False
sign_yidui = False
sign_gaopai = True

sign_A = tem_list[0]
tem_tonshua = sign_A[0]
a = Counter([i[1] for i in tem_list])
index_list = []
for i in tem_list:
    index_list.append(kapai_list.index(i[1:]))
index_list = sorted(index_list)
# 同花
for i in tem_list[1:]:
    if i[0] != tem_tonshua:
        sign_tonghua = False
        break
    tem_tonshua = i[0]

if not sign_tonghua:
    if len(a) == n:

        tem_number = index_list[0]
        for i in index_list[1:]:
            if i - tem_number != 1:
                sign_shunzi = False
                break
            tem_number = i
    else:
        sign_shunzi = False
else:
    if len(a) == n:

        if index_list[0] == 0:
            if index_list[-1] == 12:
                tem_shun = index_list[1]
                for i in index_list[2:]:
                    if i - tem_shun != 1:
                        sign_HuangJiaTongHuaShun = False
                        break
                    tem_shun = i
            else:
                sign_HuangJiaTongHuaShun = False
        else:
            sign_HuangJiaTongHuaShun = False

        if sign_tonghua and not sign_HuangJiaTongHuaShun:
            tem_shun = index_list[0]
            for i in index_list[1:]:
                if i - tem_shun != 1:
                    sign_tonghuashun = False
                    break
                tem_shun = i
        else:
            sign_tonghuashun = False

        if sign_HuangJiaTongHuaShun:
            print("HuangJiaTongHuaShun")
            sign_gaopai = False
        elif sign_tonghuashun:
            print("TongHuaShun")
            sign_gaopai = False



count_list = []
for i in a:
    count_list.append(a[i])

if (4 in count_list and( 2 in count_list or 3 in count_list)) or (3 in count_list and (2 in count_list or count_list.count(3) > 1)):
    sign_hulu = True
    print("HuLu")
    sign_gaopai = False
elif 4 in count_list and n - len(a) == 3:
    sign_sitiao = True
    print("SiTiao")
    sign_gaopai = False

if sign_tonghua and not sign_sitiao and not sign_hulu and not sign_HuangJiaTongHuaShun and not sign_tonghuashun:
    print("TongHua")
    sign_gaopai = False

if not sign_tonghua and sign_shunzi:
    print("ShunZi")
    sign_gaopai = False

if not sign_tonghua:
    if 3 in count_list and n - len(a) <= 2:
        sign_santiao = True
        print("SanTiao")
        sign_gaopai = False
    elif count_list.count(2) == 2 and n - len(a) <= 2:
        sign_liangdui = True
        print("LiangDui")
        sign_gaopai = False
    elif count_list.count(2) == 1 and n - len(a) <= 1:
        sign_yidui = True
        print("YiDui")
        sign_gaopai = False

if sign_gaopai:
    print("GaoPai")
