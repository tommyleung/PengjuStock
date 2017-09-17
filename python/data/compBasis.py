# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import urllib

import rpc

# 公司基本经营信息获取
print '更新公司基本信息:', str(sys.argv[1]), str(sys.argv[2])

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

finalcialUrl = 'https://xueqiu.com/stock/f10/compinfo.json?symbol=' + stockCodes + '&page=1&size=4&_=150313634190'
httpMethod = 'GET'

# 获取数据
decode = rpc.getResponse(finalcialUrl, httpMethod, data)
company = decode['tqCompInfo']

#公司地址
addr = company['officeaddr']
officeAddr = company['officeaddr']

#公司名称
compname = company['compname']
#公司简介
companyIntro = company['compintro']
#主营业务
majorBusiness = company['majorbiz']

#创建时间
founddate = company['founddate']
#组织类型
orgtype = company['orgtype']
#注册资金
regcapital = company['regcapital'] * 10000

print '地址:', addr
print '公司名称:', compname
print '成立日期:', founddate
print '机构类型:', orgtype
print '注册资本:', regcapital
print '公司简介:', companyIntro
print '主营业务:', majorBusiness

quit()

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
        cursor.execute(sql, (stockCode, '22', i['reportdate'], '期末现金及现金等价物余额', i['cashequfinbal'], reportSeason))
        db.commit()

except Exception, e:
    print e
    db.rollback()
finally:
    print '数据更新完毕......'
    cursor.close()
    db.close();
