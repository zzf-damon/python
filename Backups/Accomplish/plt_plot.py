import matplotlib.pyplot as plt

# %%
# plt.plot()函数的本质就是根据点连接线。根据x(数组或者列表) 和 y(数组或者列表)组成点，然后连接成线。


x = [1, 2, 3, 4]
y = [1, 2, 20, 50]
# 创建一个画布
plt.figure()
# 创建一条线
plt.plot(x, y)

# 展现画布
plt.show()
# %%
# 缺省x的情况下，x的默认值是：range(len(y))


# 缺省x参数时，默认的x是range(len(y))
y = [1, 2, 3, 4]
# 创建一个画布
plt.figure()
# 创建一条线
plt.plot(y)
# 展现画布
plt.show()

# %%
# fixme 线形 颜色 控制符
"""
字符	颜色
'b'	blue
'g'	green
'r'	red
'c'	cyan 青色
'm'	magenta平红
'y'	yellow
'k'	black
'w'	white


字符	类型
'-'	实线
'--'	虚线
'-.'	虚点线
':'	点线
' '	空类型，不显示线
"""

x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]
y4 = [1, 16, 81, 124]
# 创建一个画布
plt.figure()
# 在figure下线
plt.plot(x, y1, "-or") #实线
plt.plot(x, y2, "--y") #虚线
plt.plot(x, y3, "-.y") #虚点线
plt.plot(x, y4, ":ob") # 点线
# 展现画布
plt.show()

# %%
# fixme 普通的点
"""
'.'	点
','	像素点
'o'	原点
"""

x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]
y4 = [1, 16, 81, 124]
# 创建一个画布
plt.figure()
# 在figure下的线
plt.plot(x, y1, "-.") # 点
plt.plot(x, y2, "-,") # 像素点
plt.plot(x, y3, "-o") # 圆点

# 展现画布
plt.show()
# %%
# fixme 三角点
"""
'^'	上三角点
'v'	下三角点
'<'	左三角点
'>'	右三角点
"""
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]
y4 = [1, 16, 81, 124]
# 创建一个画布
# plt.figure()
# 在figure下的线
plt.plot(x, y1, "-^")
plt.plot(x, y2, "-v")
plt.plot(x, y3, "-<")
plt.plot(x, y4, "->")

# 展现画布
plt.show()
# %%
# fixme 三叉点
"""

'1'	下三叉点
'2'	上三叉点
'3'	左三叉点
'4'	右三叉点
"""
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]
y4 = [1, 16, 81, 124]
# 创建一个画布
plt.figure()
# 在figure下的线
plt.plot(x, y1, "-1")
plt.plot(x, y2, "-2")
plt.plot(x, y3, "-3")
plt.plot(x, y4, "-4")

# 展现画布
plt.show()

# %%
# fixme 多边形点
"""
's'	正方点
'p'	五角点
'*'	星形点
'h'	六边形1
'H'	六边形2
"""
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]
y4 = [1, 16, 81, 124]
y5 = [1, 64, 100, 180]
# 创建一个画布
plt.figure()
# 在figure下的线
plt.plot(x, y1, "-s")
plt.plot(x, y2, "-p")
plt.plot(x, y3, "-*")
plt.plot(x, y4, "-h")
plt.plot(x, y5, "-H")

# 展现画布
plt.show()

# %%
# fixme 其他

"""

'+'	加号点
'x'	乘号点
'D'	实心菱形点
'd'	细菱形点
'_'	横线点
'|'	竖线点
"""
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]
y4 = [1, 16, 81, 124]
y5 = [1, 64, 100, 180]
# 创建一个画布
plt.figure()
# 在figure下的线
plt.plot(x, y1, "-+")
plt.plot(x, y2, "-x")
plt.plot(x, y3, "-D")
plt.plot(x, y4, "-d")
plt.plot(x, y5, "-_")

# 展现画布
plt.show()

# %%
# fixme 其他
import numpy as np
"""
color="green" 指定颜色为绿色

linestyle="dashed" 指定线形为dashed类型

marker="o" 指定标记类型为o点

markerfacecolor="blue"指定标记的颜色为蓝色

markersize=20 指定标记的大小为20
"""
x = np.arange(10)
y1 = x * 1.5
y2 = x * 2.5
y3 = x * 3.5
y4 = x * 4.5
y5 = x * 5.5

plt.plot(x, y1, "-P")
plt.plot(x, y2, "-|")
plt.plot(x, y3, color="#000000")
plt.plot(x, y4, "-o", markersize=20)
plt.plot(x, y5, "-^", markerfacecolor="blue")

plt.show()
# %%
x = [[1,2],[3,4]]
plt.plot(1,2,"<")
plt.show()