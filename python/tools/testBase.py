# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
import numpy.linalg as npl
import pybrain as pb

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer

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

#反向传播训练
'''
net = buildNetwork(2, 3, 1, bias=False, hiddenclass=TanhLayer)

print net.activate((1, 1))

print 'net:', net
print 'net[in]:', net['in'], 'net[hidden]:', net['hidden0'], 'net[out]:', net['out']
print 'Modules:', net.modules

print 'Connections:', net.connections
print 'Connections1:', net.connections.items()[0]

for conn in net.connections.items():
    print 'connection:', conn

# 构建训练集, 输入2节点, 输出为1节点
ds = SupervisedDataSet(2, 1)
ds.addSample((0, 0), (0,))
# ds.addSample((1, 1), (2,))
ds.addSample((1, 0), (1,))
# ds.addSample((0, 1), (1,))
print ds

#开始训练
trainer = BackpropTrainer(net, ds, verbose=True, learningrate=0.01)
# print trainer

#trainer.trainUntilConvergence()
print 'net after trainer:\n', net

print net.activate((0, 0)), ', real:0'
print net.activate((0, 1)), ', real:1'
print net.activate((1, 0)), ', real:1'
print net.activate((1, 1)), ', real:2'

'''

# feedback network
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection

# create network
fnn = FeedForwardNetwork()

# create layer
inn = LinearLayer(2)
hidden = SigmoidLayer(3)
out = LinearLayer(1)

# add modulars
fnn.addInputModule(inn)
fnn.addModule(hidden)
fnn.addOutputModule(out)

# add connection and active machine
in_hidden = FullConnection(inn, hidden)
hidden_out = FullConnection(hidden, out)
fnn.addConnection(in_hidden)
fnn.addConnection(hidden_out)
fnn.sortModules()

# examine feedback network
'''
print 'FeedBack network: ', fnn
print 'in_hidden params: ', in_hidden.params
print 'hidden_out params:', hidden_out.params
print fnn.params
'''

#for i in range(0, 10):
    # fnn.reset()
    #print 'active[2, 1]:', fnn.activate((2,1))

ds = SupervisedDataSet(2, 1)
ds.addSample([0, 0], [0])
ds.addSample([0, 1], [1])
ds.addSample([1, 0], [1])
ds.addSample([1, 1], [2])
tr = BackpropTrainer(fnn, dataset=ds, learningrate=0.01)
tr.trainUntilConvergence()

for i in range(0, 10):
    print fnn.activate((1, 1))









