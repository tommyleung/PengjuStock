# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import httplib
import urllib
import MySQLdb
import json


# 获取头部
def getHeaders():
    reqHeader = {
        'Host': 'xueqiu.com',
        'Cookie': 'device_id=66c2d36007ff06e2686dc5555681b887; s=g413wj53q7; __utma=1.484125305.1503102157.1504957323.1505613645.9; __utmz=1.1503102157.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAJcGrVUIXAEAw0/EKp0QDgWVoXmf; xq_a_token=ed965d6ca0f68aa2f0b4a80a510e86fe5c02784d; xq_a_token.sig=4h-a7hDw5OAWxQatJglpF46pYf4; xq_r_token=fdcc8cfbe737cc4ba5146adb235fd757dc4acc3f; xq_r_token.sig=ZE73n9TV1mAyquMYb7qty1JIO_4; u=351506129464285; Hm_lvt_1db88642e346389874251b5a1eded6e3=1505547656,1505547665,1505613638,1506129465; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1506129465'
    }
    return reqHeader


# 获取JSON数据
def getResponse(url, method, data):
    # print url, method, data

    # 连接服务器
    conn = httplib.HTTPSConnection('xueqiu.com')
    conn.request(method, url, data, getHeaders())

    # 获取具体数据
    resp = conn.getresponse()
    status = resp.status

    if status != 200:
        print '请求数据失败'
        quit()

    entity = resp.read();
    decode = json.loads(entity)
    return decode


# 获取数据库连接
def getDBConnection():
    db = MySQLdb.connect('106.14.117.12', 'root', '123456', 'pengju_stock')
    return db


print ''
