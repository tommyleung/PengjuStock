# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
import numpy.linalg as npl

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




