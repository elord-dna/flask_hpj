import pymysql
class mysqlhelp():

    __conn = None
    __cursor = None

    def __enter__(self):
        self.__conn = pymysql.connect("111.229.3.100","root",'u4i3o2p1','lalala')
        self.__cursor = self.__conn.cursor(cursor = pymysql.cursors.DictCursor)
    
    def getConnection(self):
        if self.__conn is None:
            self.__conn = pymysql.connect("111.229.3.100","root",'u4i3o2p1','lalala')
            self.__cursor = self.__conn.cursor(cursor = pymysql.cursors.DictCursor)
        return self.__conn, self.__cursor

    def selectOne(self, sql, args):
        conn, cursor = self.getConnection()
        cursor.execute(sql, args)
        res = cursor.fetchone()
        return res
    
    def selectall(self,sql):
        conn, cursor = self.getConnection()
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    
    
    # def findById(self, uid):
    #     sql = "select * from pokemon where number = %s limit 1"
    #     return self.selectOne(sql, (uid))
    
    def close(self):
        if self.__conn:
            self.__conn.close()

        

    @staticmethod
    def find(uid,db,cur):
        sql = "select * from pokemon where number = %s"
        try:
            cur.execute(sql,uid)
            res = cur.fetchall()
            print(res)
        except:
            print("Error: unable to fetch data")
        db.close()


