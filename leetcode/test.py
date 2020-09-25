n = int(input())

total_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

list_1 = [i for i in input().split(" ")]
hs = True
tem_hs = list_1[0][0]
for i in list_1[1:]:
    if i != tem_hs:
        hs = False
        break

hjt_tem = True
s_tem = True
if hs:

    tem_s = list_1[0][0]
    if tem_s == "A" and list_1[1][0] == "K":
        tem_s = list_1[1][0]
        for i in list_1[2:]:
            if total_list.index(i) - total_list.index(tem_s) != 1:
                hjt_tem = False
                break
    else:
        for i in list_1[1:]:
            if total_list.index(i) - total_list.index(tem_s) != 1:
                s_tem = False
                break


"""
HuangJiaTongHuaShun、TongHuaShun、SiTiao、HuLu、TongHua、ShunZi、SanTiao、LiangDui、YiDui、GaoPai
"""

if hjt_tem:
    print("HuangJiaTongHuaShun")
elif s_tem:
    print("TongHuaShun")
elif hs:
    print("TongHua")
else:
    st_tem = True

