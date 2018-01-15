# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import httplib
import urllib
# import MySQLdb
import json
import pymysql as mysql


# 获取头部
def getHeaders():
    reqHeader = {
        'Host': 'xueqiu.com',
        'Cookie': 'device_id=d969dc896ad8a8f880e82525c396bcb9; __utma=1.1483386770.1502702541.1502702541.1502702541.1; __utmz=1.1502702541.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAP6pSQdNigAA4rJfZXiYiJCKRa3M; xq_a_token=93ef7d84fd99d7b5f81ea4e1442c7252dff29d20; xq_a_token.sig=2_cWCFNwc-q7CurYUzOoewHw_DM; xq_r_token=18ddc4996d6018b400ebaaaa74f144296c288826; xq_r_token.sig=7749cnGDm8cToOaVZtCC3FKmJys; u=501515634639072; Hm_lvt_1db88642e346389874251b5a1eded6e3=1515140029,1515634640,1515634646; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1515634646'
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
    db = MySQLdb.connect()
    return db

def getPyMySQLConnection():
    conn = mysql.connect()
    return conn

print ''
