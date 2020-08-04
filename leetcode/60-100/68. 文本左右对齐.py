words1 = ["a","b","c","d","e"]

maxWidth1 = 1

text = "justification. "


def split_w(tem_s, maxWidth):
    list1 = tem_s.split(" ")
    if len(list1) == 1:
        return tem_s + " " * (maxWidth - len(tem_s))
    n = len(list1) - 1
    length = maxWidth - len(tem_s) + n
    mod = length % n
    quotient = length // n
    res = ""
    for i in list1[:-1]:
        s = 1 if mod != 0 else 0
        res += i + " " * quotient + " " * s
        if mod != 0:
            mod -= 1
    return res + list1[-1]


def fullJustify(words, maxWidth: int):
    res = []
    if not words: return []
    tem_res = words[0]
    for word in words[1:]:
        if len(word) < maxWidth:
            if len(tem_res + word) < maxWidth:
                tem_res += " " + word
            else:
                res.append(split_w(tem_res, maxWidth))
                tem_res = word
        else:
            res.append(split_w(tem_res, maxWidth))
            tem_res = word
    res.append(tem_res + " " * (maxWidth - len(tem_res)))
    return res


print(fullJustify(words1, maxWidth1))
