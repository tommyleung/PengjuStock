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
        'Cookie': 'device_id=66c2d36007ff06e2686dc5555681b887; s=g413wj53q7; __utma=1.484125305.1503102157.1503230423.1504957323.8; __utmz=1.1503102157.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAALQe+CamBQAAMPSh0/Us746C9WXz; xq_a_token=7df3040e6c1713de2145a1362593660977fa30dd; xq_a_token.sig=8DqzggN2gD54BWc8DMaH9luL8vM; xq_r_token=734bcfccb40a6608ddf341bbbaab311be06259a0; xq_r_token.sig=SlmUqY51MyeEBDdgvLLwRtOgJcU; u=641505547655845; Hm_lvt_1db88642e346389874251b5a1eded6e3=1503117111,1504957313,1505002655,1505547656; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1505547656'
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
