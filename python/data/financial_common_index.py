# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import urllib
import time

import rpc

# 主要财务指标数据接口
#print '更新公司财务数据:', str(sys.argv[1]), str(sys.argv[2])

# 参数
reqdata = {
    'symbol': 'SZ002561',
    'page': 1,
    'size': 1,
    '_': 1502605245564
}
data = urllib.urlencode(reqdata)

stockCode = sys.argv[2]
stockCodes = sys.argv[1] + sys.argv[2]

def addData(tableType, data, cursor, db, description, dateName):
    print '开始更新数据' + description
    # 删除数据
    sql = 'delete from stock_financial_common_index where stock_code = %s and table_type = %s'
    cursor.execute(sql, (stockCodes, tableType))
    db.commit

    for i in data['list']:
        # 新增数据
        sql = "insert into stock_financial_common_index(stock_code, index_id, create_date, " \
              "index_name, index_value, index_season, index_code, table_type)" \
              " VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

        print str(i[dateName]) + '数据更新'

        # 季度计算
        reportdate = i[dateName];
        reportSeason = ''
        if reportdate.find('0331') >= 0:
            reportSeason = reportdate[0:4] + 'y' + '1s'
        elif reportdate.find('0630') >= 0:
            reportSeason = reportdate[0:4] + 'y' + '2s'
        elif reportdate.find('0930') >= 0:
            reportSeason = reportdate[0:4] + '-' + '3s'
        else:
            reportSeason = reportdate[0:4] + 'y' + '4s'

        # 提交数据
        for key in i.keys():
            # 操作数据库
            cursor.execute(sql, (stockCodes, '1', i[dateName], '', i[key], reportSeason, key, tableType))

        db.commit()

# 开始更新财务指标信息
def doDataUpdate():
    times = str(int(time.time()))

    # 损益表
    finalcialIncreaseUrl = 'https://xueqiu.com/stock/f10/incstatement.json?symbol=' \
                   + stockCodes + '&page=1&size=500&_=' + times
    finalcialDebatUrl = 'https://xueqiu.com/stock/f10/balsheet.json?symbol=' \
                   + stockCodes + '&page=1&size=500&_=' + times
    finalcialCashUrl = 'https://xueqiu.com/stock/f10/cfstatement.json?symbol=' \
                   + stockCodes + '&page=1&size=500&_=' + times

    # 获取数据
    httpMethod = 'GET'
    decode = rpc.getResponse(finalcialIncreaseUrl, httpMethod, data)
    decode2 = rpc.getResponse(finalcialDebatUrl, httpMethod, data)
    decode3 = rpc.getResponse(finalcialCashUrl, httpMethod, data)

    # 打开数据库连接
    db = rpc.getPyMySQLConnection()

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # 更新损益财务指标
        addData(tableType='1', data=decode, cursor=cursor, db=db, description='利润指标', dateName='enddate');
        # 更新负债指标
        addData(tableType='2', data=decode2, cursor=cursor, db=db, description='负债指标', dateName='reportdate');
        # 更新现金流指标
        addData(tableType='3', data=decode3, cursor=cursor, db=db, description='现金流指标', dateName='enddate');
    except Exception, e:
        print e;
        db.rollback();
    finally:
        print '数据更新完毕......';
        cursor.close();
        db.close();

# 开始数据更新
doDataUpdate();