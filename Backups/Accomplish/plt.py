# import torch
# import torch.nn as nn
# import numpy as np
# import matplotlib.pyplot as plt
# from torch.autograd import Variable
# input_size = 1
# output_size = 1
# learning_rate = 0.001
# xtrain = np.array([[2.3],[4.4],[3.7],[6.1],[7.3],[2.1],[5.6],[7.7],[8.7],[4.1],[6.7],[6.1],[7.5],[2.1],[7.2],[5.6],[5.7],[7.7],[3.1]],dtype=np.float32)
# ytrain = np.array([[3.7],[4.76],[4.],[7.1],[8.6],[3.5],[5.4],[7.6],[7.9],[5.3],[7.3],[7.5],[8.5],[3.2],[8.7],[6.4],[6.6],[7.9],[5.3]],dtype=np.float32)
# plt.figure()
# plt.xlabel("xtrain")
# plt.ylabel("ytrain")
# plt.show()


# import torch
# import matplotlib.pyplot as plt
#
# x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
# y = 3 * x + 10 + torch.rand(x.size())
# # 上面这行代码是制造出接近y=3x+10的数据集，后面加上torch.rand()函数制造噪音
# print(x)
# print(y)
# # 画图
# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24

np.random.seed(42)

# x轴的采样点
x = np.linspace(0, 5, 100)

# 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……
y = 2 * np.sin(x) + 0.3 * x ** 2
y_data = y + np.random.normal(scale=0.3, size=100)
print(x)
print(y)
# figure()指定图表名称
plt.figure('data')

# '.'标明画散点图，每个散点的形状是个圆
plt.plot(x, y_data, '.')

# 画模型的图，plot函数默认画连线图
plt.figure('model')
plt.plot(x, y)

# 两个图画一起
plt.figure('data & model')

# 通过'k'指定线的颜色，lw指定线的宽度
# 第三个参数除了颜色也可以指定线形，比如'r--'表示红色虚线
# 更多属性可以参考官网：http://matplotlib.org/api/pyplot_api.html
plt.plot(x, y, 'k', lw=3)

# scatter可以更容易地生成散点图
plt.scatter(x, y_data)

# 将当前figure的图保存到文件result.png
# plt.savefig('result.png')

# 一定要加上这句才能让画好的图显示在屏幕上
plt.show()



a = [1, 2, 3, 4] # y 是 a的值，x是各个元素的索引
b = [5, 6, 7, 8]

plt.plot(a, b, 'r--', label = 'aa')
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.title('this is a demo')
plt.legend() # 将样例显示出来

plt.plot()
plt.show()



from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
url = "http://www.yizuren.com//d/file/p/2016/08/af81bc1b12f4d9e690db6eee02e85af9.jpg"
response = requests.get(url).content
with open("./2.jpg","wb") as f:
    f.write(response)
img = Image.open("./2.jpg")
img.show()

#
# image = Image.open(BytesIO(response.content))
# image.show()
import urllib3
from skimage import io
# image = "1.jpg"
# response = requests.get("http://www.yizuren.com//d/file/p/2016/08/af81bc1b12f4d9e690db6eee02e85af9.jpg").content
# image = io.imread(response)
# io.imshow(image)
# io.show()
# requests.urlretrieve(url, )




