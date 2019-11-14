import pymysql


class DBConnect:

    def get_connect(self,host, port, user, password,db):
        #连接mysql初始化连接
        conn = pymysql.connect(host=host, port=int(port),user=user, password=password, database=db,charset='utf8')
        cursor  = conn.cursor()   #初始化游标
        sql = 'show databases'
        cursor.execute(sql)
        text = cursor.fetchall()
        print(text)
        return text