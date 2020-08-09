def palindromePairs(words):
    if len(words) < 2: return []
    res = []
    for i, word_i in enumerate(words):
        for j, word_j in enumerate(words):
            if i == j:continue
            str1 = word_i+word_j
            if str1 == str1[::-1]:
                res.append([i,j])
    return res



def palindromePairs1(words):
    if len(words) < 2: return []
    res = []
    for i, word_i in enumerate(words):
        index = words.index(word_i[::-1])



    return res



words_List = ["abcd", "dcba", "lls", "s", "sssll"]

print(palindromePairs1(words_List))
