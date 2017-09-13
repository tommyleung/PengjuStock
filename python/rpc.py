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
        'Cookie': 'device_id=66c2d36007ff06e2686dc5555681b887; s=g413wj53q7; __utma=1.484125305.1503102157.1503230423.1504957323.8; __utmz=1.1503102157.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAN+PIlRL6gEAldOutOhktPAp2jpH; xq_a_token=f8846a20e3a8074cd781524d47619ba6879990e2; xq_a_token.sig=F2iHnlcpCSXgutP8euxdQqDfqq4; xq_r_token=562674ae525074f694a9961c5a49a644275e3b53; xq_r_token.sig=ZcCuq7XTdkGNIafT5ot8irXZzCU; u=461505002654313; Hm_lvt_1db88642e346389874251b5a1eded6e3=1503102157,1503117111,1504957313,1505002655; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1505002655'
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
