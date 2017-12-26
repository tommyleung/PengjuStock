# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 中文分词工具
import jieba
seg_list = jieba.cut("我来到北京清华大学")
print "/".join(seg_list)

import jieba.posseg as posseg
words = posseg.cut("我来到你的城市，走过你来时的路")
for word, seg in words:
    print word, seg
