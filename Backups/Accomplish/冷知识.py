# 急速合并列表
a = [1,2]
b = [3,4]
c = [5,6]
print(sum((a,b,c), []))


# Python 3.9 新特性
profile = {"name": "xiaoming", "age": 27}
ext_info = {"gender": "male"}
profile | ext_info
ext_info |= profile


# 条件语句
age1 = 20
msg1 = age1 > 18 and "已成年" or "未成年"
msg1 = ("未成年", "已成年")[age1 > 18]
msg1 = {True: "已成年", False: "未成年"}[age1 > 18]

