# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#引入机器学习包
import pybrain as pyb
import sklearn as skl
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn.datasets as ds
import sklearn.linear_model as lm
import matplotlib

#决策线
def plot_decision_boundary(X, Y, model):
    # X - some data in 2dimensional np.array
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))

    # here "model" is your model's prediction (classification) function
    Z = model(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis('off')

    for i in x:
        print i

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)


#随机数据集生成
np.random.seed(0)
x, y = ds.make_moons(200, noise=0.20)
plt.scatter(x[:, 0], x[:, 1], s=40, c=y, cmap=plt.cm.Spectral)

clf = skl.linear_model.LogisticRegressionCV()
clf.fit(x, y)


# Plot the decision boundary
plot_decision_boundary(x, y, lambda x: clf.predict(x))
plt.title("Logistic Regression")
plt.show()