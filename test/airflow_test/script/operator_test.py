# from pyspark.conf import SparkConf
# from pyspark import SparkContext
# from pyspark import HiveContext
# from pyspark.sql import SparkSession
import re
import configparser


def read_sql(path):
    #去读取监控的sql文件或者是日志文件
    with open(path,'r',encoding='urf-8') as text_response:
        text = text_response.read()
    return text


def read_log(path):
    #读取日志文件,找增量mark
    with open(path,'r',encoding='utf-8') as log_response:
        logs_text = log_response.readlines()
        Increment_mark = logs_text[-1].strip('\n').split('|')[3]
    return Increment_mark


def get_search(text):


def get_connect(host, port, user, password, db,sql):
    # 连接mysql初始化连接
    conn = pymysql.connect(host=host, port=int(port), user=user, password=password, database=db, charset='utf8')
    cursor = conn.cursor()  # 初始化游标
    cursor.execute(sql)
    text = cursor.fetchall()
    print(text)
    return text

def get_test(sqoopIncrementField,sqoopIncrementInterval,sqoopTable):
    executeSql ="select case when max("+ sqoopIncrementField +") like '%-%' then convert(nvarchar(7),dateadd(month,-"+sqoopIncrementInterval+",concat(max("+sqoopIncrementField+"),'-01')),23) else convert(nvarchar(6),dateadd(month,-"+sqoopIncrementInterval+",concat(SUBSTRING(max("+sqoopIncrementField+"),1,4),'-', SUBSTRING(max("+sqoopIncrementField +"),5,2),'-01')),112) end from " + sqoopTable
    print(executeSql)

if __name__ == '__main__':
    log_path = r'C:\Users\yj\Desktop\test.log'
    mark = read_log(log_path)
    get_test('2018-11-25',mark,'temp')
    print(mark)




