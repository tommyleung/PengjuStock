import json
import rpc

s = json.loads('{"name":"test"}');
print s.keys(), s.values(), s['name']

fileOpen = open('../../shell/json.txt');
text = '';
try:
    text = fileOpen.read();
finally:
    fileOpen.close();

print text;

dict = json.loads(text);
#print dict;

db = rpc.getPyMySQLConnection();
cursor = db.cursor();

try:
    cursor.execute('delete from stock_index_dict where 1=1');
    db.commit();
    for dic in dict:
        try:
            sql = "insert into stock_index_dict(index_name, index_unit, index_descriptor, " \
                  "index_code, index_type, index_type1) " \
                  "values(%s, %s, %s, %s, %s, %s)";
            # print dic;
            cursor.execute(sql, (dic["value"], "", dic["value"], dic["key"], dic["type"], dic["type1"]));
        except Exception, e:
            print e;
            print dic;
    db.commit();
except Exception, e:
    print e;
    db.rollback();
finally:
    cursor.close();
    db.close();

