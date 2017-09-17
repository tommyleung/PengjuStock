# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import urllib

import rpc

# 主要财务指标数据接口
print '更新股票财务数据:', str(sys.argv[1]), str(sys.argv[2])

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

finalcialUrl = 'https://xueqiu.com/stock/f10/finmainindex.json?symbol=' + stockCodes + '&page=1&size=500&_=1502605245564'
httpMethod = 'GET'

# 获取数据
decode = rpc.getResponse(finalcialUrl, httpMethod, data)

# 打开数据库连接
db = rpc.getDBConnection()

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

try:
    print '开始更新数据......'

    # 删除数据
    sql = 'delete from stock_financial_index where stock_code = %s'
    cursor.execute(sql, (stockCode))
    db.commit

    for i in decode['list']:
        # 新增数据
        sql = "insert into stock_financial_index(stock_code, index_id, create_date, index_name, index_value, index_season) VALUES(%s, %s, %s, %s, %s, %s)"

        print str(i['reportdate']) + '数据更新'

        # 季度计算
        reportdate = i['reportdate'];
        reportSeason = ''
        if reportdate.find('0331') >= 0:
            reportSeason = reportdate[0:4] + 'y' + '1s'
        elif reportdate.find('0631') >= 0:
            reportSeason = reportdate[0:4] + 'y' + '2s'
        elif reportdate.find('0931') >= 0:
            reportSeason = reportdate[0:4] + '-' + '3s'
        else:
            reportSeason = reportdate[0:4] + 'y' + '4s'

        # 操作数据库
        cursor.execute(sql, (stockCode, '1', i['reportdate'], '每股收益', i['basiceps'], reportSeason))
        cursor.execute(sql, (stockCode, '2', i['reportdate'], '每股净资产', i['naps'], reportSeason))

        # print '每股现金流: ' + str(i['peropecashpershare'])
        cursor.execute(sql, (stockCode, '3', i['reportdate'], '每股现金流', i['peropecashpershare'], reportSeason))

        # print '每股经营现金流：' + str(i['peropecashpershare'])
        cursor.execute(sql, (stockCode, '4', i['reportdate'], '每股经营现金流', i['peropecashpershare'], reportSeason))

        # print '净资产增长率：' + str(i['netassgrowrate'])
        cursor.execute(sql, (stockCode, '5', i['reportdate'], '净资产增长率', i['netassgrowrate'], reportSeason))

        # print '净资产收益率(加权)(%): ' + str(i['weightedroe'])
        cursor.execute(sql, (stockCode, '6', i['reportdate'], '净资产收益率(加权)', i['weightedroe'], reportSeason))

        # print '主营业务收入增长率(%): ' + str(i['mainbusincgrowrate'])
        cursor.execute(sql, (stockCode, '7', i['reportdate'], '净资产收益率(加权)', i['weightedroe'], reportSeason))

        # print '净利润增长率：' + str(i['netincgrowrate'])
        cursor.execute(sql, (stockCode, '8', i['reportdate'], '净利润增长率', i['netincgrowrate'], reportSeason))

        # print '总资产增长率(%): ' + str(i['totassgrowrate'])
        cursor.execute(sql, (stockCode, '9', i['reportdate'], '总资产增长率', i['totassgrowrate'], reportSeason))

        # print '销售毛利率(%): ' + str(i['salegrossprofitrto'])
        cursor.execute(sql, (stockCode, '10', i['reportdate'], '销售毛利率', i['salegrossprofitrto'], reportSeason))

        # print '主营业务收入: ' + str(i['mainbusiincome'])
        cursor.execute(sql, (stockCode, '11', i['reportdate'], '主营业务收入', i['mainbusiincome'], reportSeason))

        # print '主营业务利润: ' + str(i['mainbusiprofit'])
        cursor.execute(sql, (stockCode, '12', i['reportdate'], '主营业务利润', i['mainbusiprofit'], reportSeason))

        # print '利润总额: ' + str(i['totprofit'])
        cursor.execute(sql, (stockCode, '13', i['reportdate'], '利润总额', i['totprofit'], reportSeason))

        # print '净利润: ' + str(i['netprofit'])
        cursor.execute(sql, (stockCode, '14', i['reportdate'], '净利润', i['netprofit'], reportSeason))

        # print '资产总额: ' + str(i['totalassets'])
        cursor.execute(sql, (stockCode, '15', i['reportdate'], '资产总额', i['totalassets'], reportSeason))

        # print '负债总额：' + str(i['totalliab'])
        cursor.execute(sql, (stockCode, '16', i['reportdate'], '负债总额', i['totalliab'], reportSeason))

        # print '股东权益合计:' + str(i['totsharequi'])
        cursor.execute(sql, (stockCode, '17', i['reportdate'], '股东权益合计', i['totsharequi'], reportSeason))

        # print '经营活动产生的现金流量净额: ' + str(i['operrevenue'])
        cursor.execute(sql, (stockCode, '18', i['reportdate'], '经营活动产生的现金流量净额', i['operrevenue'], reportSeason))

        # print '投资活动产生的现金流量净额: ' + str(i['invnetcashflow'])
        cursor.execute(sql, (stockCode, '19', i['reportdate'], '投资活动产生的现金流量净额', i['invnetcashflow'], reportSeason))

        # print '筹资活动产生的现金流量净额：' + str(i['finnetcflow'])
        cursor.execute(sql, (stockCode, '20', i['reportdate'], '筹资活动产生的现金流量净额', i['finnetcflow'], reportSeason))

        # print '现金及现金等价物净增加额: ' + str(i['cashnetr'])
        cursor.execute(sql, (stockCode, '21', i['reportdate'], '现金及现金等价物净增加额', i['cashnetr'], reportSeason))

        # print '期末现金及现金等价物余额: ' + str(i['cashequfinbal'])
        cursor.execute(sql, (stockCode, '22', i['reportdate'], '期末现金及现金等价物余额', i['cashequfinbal'], reportSeason))
        db.commit()

except Exception, e:
    print e
    db.rollback()
finally:
    print '数据更新完毕......'
    cursor.close()
    db.close();
