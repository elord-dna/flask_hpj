from pysql import mysqlhelp

_helper = mysqlhelp()

def findById(uid):
    sql = "select * from pokemon where number = %s limit 1"
    return _helper.selectOne(sql, uid)

def findall():
    sql = "select * from pokemon limit 50"
    return _helper.selectall(sql)
    