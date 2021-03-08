def cut(s,k):
    results = [ ]
    for x in range (k-1, len ( s ) ) :
        for i in range(len(s)-x):
            results.append(s[i:i+x+1])
    return results
lenth = int(input())
words = input()
a = cut(words,lenth)
num =[]
for word in a:
    num.append(words.count(word))
print(a[num.index(max(num))])