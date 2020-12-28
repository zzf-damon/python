from pyhanlp import *
from collections import Counter

with open("./Datas/data.txt", "r", encoding='utf-8') as f:
    contents, labels = list(), list()
    for i in f.readlines():
        tem_list = i.strip("\n").split("\t")
        assert len(tem_list) == 2
        contents.append(tem_list[0])
        labels.append(int(tem_list[1]))

    print(Counter(labels), len(labels))

ClusterAnalyzer = SafeJClass('com.hankcs.hanlp.mining.cluster.ClusterAnalyzer')
analyzer = ClusterAnalyzer()

for i in range(len(labels)):
    analyzer.addDocument(i, contents[i])
a = [list(i) for i in analyzer.repeatedBisection(10)]
print([len(i) for i in a])
