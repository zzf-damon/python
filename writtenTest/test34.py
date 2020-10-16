import re


def check_filter(keywords, text):
    return re.sub("|".join(keywords), "*", text)  # 是用正则进行特换，第一个是正则表达式，第二个是替换字符，第三个是原字符


keywords = input()  # 句子
text =input() # 词
print(check_filter(keywords, text)) # 对了