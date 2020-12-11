import pandas as pd

# fixme 创建数据
input_data = {'n1': ["b", "a", "c", "f"],
              'n2': ["a", "b", "d", "e"],
              'w': [19, 20, 6, 7]}

data_raw = pd.DataFrame(input_data)
print(data_raw)


# fixme 去重
def func(a, b):
    return "".join(sorted([a, b]))


data_raw2 = data_raw.copy()
data_raw2['n12'] = data_raw2.apply(lambda x: func(x.n1, x.n2), axis=1)
data_raw2.drop_duplicates(subset=['n12'], keep='first', inplace=True)
data_raw2.drop(labels=["w", "n12"], axis=1, inplace=True)
print(data_raw2)

# fixme 计算和
data_raw3 = data_raw.copy()
data_raw3['n12'] = data_raw3.apply(lambda x: func(x.n1, x.n2), axis=1)
data_raw2['w'] = [i for i in data_raw3['w'].groupby([data_raw3['n12']]).sum()]
print(data_raw2)
