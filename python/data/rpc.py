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
        'Cookie': 's=eu1a0y8gx5; device_id=d969dc896ad8a8f880e82525c396bcb9; __utma=1.1483386770.1502702541.1502702541.1502702541.1; __utmz=1.1502702541.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAL+9oXHrAgwA4rJfZc4EdPr2pash; xq_a_token=a8d434ddd975f5752965fa782596bd0b5b008376; xq_a_token.sig=ke78qTMMk1J4blZPe-jY53Uy9Ec; xq_r_token=437547d929e3cc54630bfd58136879694e1ae4a9; xq_r_token.sig=iYuNwCitZuVpyfkOu6_LLtaQn6E; u=711512698988819; Hm_lvt_1db88642e346389874251b5a1eded6e3=1511752664,1511854758,1512698990; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1512698990'
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
