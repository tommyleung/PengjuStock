# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24

np.random.seed(42)

# x轴的采样点
x = np.linspace(0, 5, 100)
print 'x:', x

# 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……
y = 2 * np.sin(x) + 0.3 * x ** 2
print 'y:', y


y_data = y + np.random.normal(scale=0.3, size=100)
print 'y_data:', y_data


# figure()指定图表名称
#plt.figure('data')

# '.'标明画散点图，每个散点的形状是个圆
#plt.plot(x, y_data, '.')
#plt.show()


# 画模型的图，plot函数默认画连线图
#plt.figure('model')
#plt.plot(x, y)
#plt.show()

# 两个图画一起
plt.figure('data & model')

# 通过'k'指定线的颜色，lw指定线的宽度
# 第三个参数除了颜色也可以指定线形，比如'r--'表示红色虚线
# 更多属性可以参考官网：http://matplotlib.org/api/pyplot_api.html
plt.plot(x, y, 'k', lw=3)

# scatter可以更容易地生成散点图
plt.scatter(x, y_data)

# 一定要加上这句才能让画好的图显示在屏幕上
plt.show()
