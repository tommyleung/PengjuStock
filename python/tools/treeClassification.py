# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sklearn
import sklearn.tree as tree
import logRegres
import matplotlib.pyplot as plt
import numpy as np

# sigmoid function
def nonlin(x, deriv=False):
    if (deriv == True):
        return np.exp(-x) * (1 + np.exp(-x))
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output dataset
y = np.array([[1, 1, 0, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1

print 'X:', X
print 'y:', y
print 'syn0:', syn0

# matrix multiplicative
print 'dot:', np.dot(X, syn0)
print 'dot:', logRegres.sigmoid(np.dot(X, syn0))

for iterator in xrange(1000):
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmssoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)

print "Output After Training:"
print 'li:', l1, '\nsyn0:', syn0
