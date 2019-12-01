# from pyspark.conf import SparkConf
# from pyspark import SparkContext
# from pyspark import HiveContext
# from pyspark.sql import SparkSession
import re
import configparser
import pymysql
import pymssql

config_path = r''
def read_sql(path):
    #去读取sql文件
    with open(path,'r',encoding='urf-8') as text_response:
        text = text_response.read()
    return text


def read_log(path, line_number, index_number):
    #读取日志文件,找增量mark

    with open(path,'r',encoding='utf-8') as log_response:
        logs_text = log_response.readlines()
        Increment_mark = logs_text[line_number].strip('\n').split('|')[index_number]
    return Increment_mark


def get_search(text):
    #re 匹配策略
    pass


def get_connect(db_type, host, port, user, password, db, sql):
    # 建立sql连接，执行sql
    if db_type == 'mysql':
        # 连接mysql初始化连接
        conn = pymysql.connect(host=host, port=int(port), user=user, password=password, database=db, charset='utf8')
        cursor = conn.cursor()  # 初始化游标
        cursor.execute(sql)
        text = cursor.fetchall()
        print(text)
        return text
    elif db_type == 'sqlserver':
        conn = pymssql.connect(server=host,user=user,password=password,
                        database=db,
                        charset="GBK",
                        port=int(port)   #,tds_version='7.0'
                        )
        cursor = conn.cursor()
        cursor.execute(sql)
        text = cursor.fetchall()
        return text

# def get_test(sqoopIncrementField,sqoopIncrementInterval,sqoopTable):
#     executeSql ="select case when max("+ sqoopIncrementField +") like '%-%' then convert(nvarchar(7),dateadd(month,-"+sqoopIncrementInterval+",concat(max("+sqoopIncrementField+"),'-01')),23) else convert(nvarchar(6),dateadd(month,-"+sqoopIncrementInterval+",concat(SUBSTRING(max("+sqoopIncrementField+"),1,4),'-', SUBSTRING(max("+sqoopIncrementField +"),5,2),'-01')),112) end from " + sqoopTable
#     print(executeSql)

if __name__ == '__main__':
    log_path = r'C:\Users\Administrator\Desktop\test.log'
    start_mark = read_log(log_path, -2,4)
    end_mark = read_log(log_path,-1,2)
    # get_test('2018-11-25',mark,'temp')
    print(start_mark[0:19])
    print(end_mark)




