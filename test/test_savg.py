import sys
import configparser
import pymysql
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)
from  DBConnect import DBConnect

print('test')




conf = configparser.ConfigParser()
conf_path = r'F:\code\github_files\51bitqunt\test\config\db_config.config'
conf.read(conf_path, encoding ='utf-8')


# keys = sys.argv[1]
# print(keys)
# print(conf.get(keys,'host'))
# print(conf.get(keys,'port'))
# print(conf.get(keys,'user'))
# print(conf.get(keys,'password'))
# print(conf.get(keys,'db'))

keys = 'jd'
host_value = conf.get(keys,'host')
port_value = conf.get(keys,'port')
user_value = conf.get(keys,'user')
password_value = conf.get(keys,'password')
db_value = conf.get(keys,'db')

DBConnect.get_connect(host_value,port_value,user_value,password_value,db_value)


conn = pymysql.connect(host=host_value, port=int(port_value),user=user_value, password=password_value, database=db_value,charset='utf8')
cursor  = conn.cursor()   #初始化游标
sql = 'show databases'
cursor.execute(sql)
text = cursor.fetchall()
print(text)

