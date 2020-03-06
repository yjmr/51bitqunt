from pyspark import SparkContext
from pyspark import HiveContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
import re
import sys
import os
from configparser import ConfigParser
path_abs = os.path.dirname(__file__)
project_home = os.path.dirname(path_abs)
sys.path.append(project_home)
import pymysql
import pymssql
sys.path.append(r'/home/py_common')
import pub_module


table_config_path = project_home + r'/config/data_check.config'
def read_sql(path):
    #去读取sql文件
    with open(path,'r',encoding='urf-8') as text_response:
        text = text_response.read()
    return text

def get_transmit_date(sql_text, Max_business_date):
    #数据回刷日期回填到sql代码里面实现,然后就可以执行这个sql
    sql_text.fotmat(transmit_date=Max_business_date)
    return sql_text

def get_config(path):
    # 读取配置文件方法
    Db_config = ConfigParser()
    Db_config.read(path,encoding='utf-8')
    return Db_config


def get_iffile(ifpath):
    # 判断是否为文件，为文件返回文件内容
    if os.path.exists(ifpath):
        sql_text = read_sql(ifpath)
        return sql_text
    else:
        return ifpath


def read_log(path, line_number, index_number):
    #读取日志文件,找增量mark

    with open(path,'r',encoding='utf-8') as log_response:
        logs_text = log_response.readlines()
        Increment_mark = logs_text[line_number].strip('\n').split('|')[index_number]
    return Increment_mark


def get_search(text):
    #re 匹配策略
    pass


def get_bigquery(sql,table_name):
    # 连接spark集群，执行sql验证策略
    sc = pub_module.get_sparkContext(table_name)
    hive_text = pub_module.execute_sql(sc, sql)
    sc.stop()
    return hive_text



def get_connect(db_type, host, port, user, password, db, sql):
    # 建立db sql连接，执行sql
    if db_type == 'mysql':
        # 连接mysql初始化连接
        conn = pymysql.connect(host=host, port=int(port), user=user, password=password, database=db, charset='utf8')
        cursor = conn.cursor()  # 初始化游标
        cursor.execute(sql)
        text = cursor.fetchall()
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





def get_email(send_text,subject_text,send_email):
    # 发邮件
    # 链接邮箱服务器
    try:
        import yagmail  # pip install yagmail
    except ImportError:
        os.stem('pip install yagmail')
    yag = yagmail.SMTP(user="xxx@.com", password="授权码", host='smtp.qq.com')
    subject = subject_text + '核对不上,请核查'
    # 发送邮件
    yag.send(send_email, subject, send_text)




def search_text(path, pattern):
    with open(path,'r',encoding='utf-8') as log_file:
        table_log = log_file.read()
    text_pattern  = re.compile(pattern,re.S).findall(table_log)
    return text_pattern[-1]









if __name__ == '__main__':
    pass


    # if not sys.argv[1]:
    #     logging.error("argument can not be none,leave the program!!!")
    # else:
    #     table_key = sys.argv[1]
    # log_path = r'C:\Users\Administrator\Desktop\test.log'
    # start_mark = read_log(log_path, -2,4)
    # end_mark = read_log(log_path,-1,2)
    # # get_test('2018-11-25',mark,'temp')
    # print(start_mark[0:19])
    # print(end_mark)
    # current_table_query = get_config(table_config_path).get(table_key, 'current_table_query')
    # source_table_query = get_config(table_config_path).get(table_key, 'source_table_query')
    # source_query_type = get_config(table_config_path).get(table_key, 'source_query_type')
    # Max_business_date = get_config(table_config_path).get(table_key, 'Max_business_date')
    # log_path = get_config(table_config_path).get(table_key,'log_path')
    # if str.upper(source_query_type)  ==  str.upper('hdi'):
    #     if xxxxx : #回刷传递
    #         Max_business_date = get_bigquery(Max_business_date) # 回刷日期
    #         replace_current_table_query = get_iffile(current_table_query)
    #         current_table_query_vaule = get_bigquery(replace_current_table_query)
    #         source_table_query_vaule = get_bigquery(source_table_query)
    #         print(table_key,"|",'current_table_query|',current_table_query_vaule,'source_table_query|',source_table_query_vaule)
    #     else:
    #         pass
    #











