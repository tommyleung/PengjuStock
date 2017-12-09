# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
import sklearn as skl
import numpy.linalg as npl
import pybrain as pb

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet

print 'numpy version:' + np.__version__ + '\n'

# matrix basic calculation
# matrix definition
x = np.array([
    [0, 1, 1],
    [1, 1, 1]
]);

# matrix transpose
y = np.array([[0, 1, 1]]).T;

# matrix multiplicative
z = x.dot(y);

# print 'print x:' + x;
# print 'print y' + y;
# print 'print z' + z;

# numpy学习

# 切片
list = range(10)
# print 'list all:', list;
# print 'list[2:4]:', list[2:4]


# numpy矩阵运算
# 矩阵定义
a = np.array([[1, 0, 1], [1, 1, 1]])
# print '矩阵a:', a

# 矩阵转置
Ta = a.transpose()
# print '矩阵a转置：', Ta

# 矩阵乘法
Tm = a.dot(Ta)
# print '矩阵乘法a * Ta:', Tm


# 智能学习包
# 人工神经网络2个输入单元、3个隐藏层，1个输出单元
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer

#反向传播训练
net = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)

print net['in'], net['hidden0'], net['out']

# 构建训练集, 输入2节点, 输出为1节点
ds = SupervisedDataSet(2, 1)
ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))
print ds



#开始训练
trainer = BackpropTrainer(net, ds, verbose=False, learningrate=0.01)
# print trainer

trainer.trainUntilConvergence(maxEpochs=100)
# print 'net after trainer:\n', net

print net.activate((0, 0)), ', real:0'
print net.activate((0, 1)), ', real:1'
print net.activate((1, 0)), ', real:1'
print net.activate((1, 1)), ', real:0'








