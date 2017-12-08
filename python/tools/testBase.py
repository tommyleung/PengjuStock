# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
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

print x;
print y;
print z;




