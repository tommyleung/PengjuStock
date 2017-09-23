# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sklearn
import sklearn.tree as tree

x = [[0, 0], [1, 1]]
y = [0, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

