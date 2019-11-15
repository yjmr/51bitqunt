import sys
import configparser
import pymysql
import os
import sys
up_one_level = os.path.dirname(__file__)
base_dir_path = os.path.dirname(up_one_level)
sys.path.append(base_dir_path)
from  DBConnect import DBConnect

keys = sys.argv[1]
print(keys)
conf = configparser.ConfigParser()

conf_path = base_dir_path + r'/test/config/db_config.config'
conf.read(conf_path, encoding ='utf-8')

host_value = conf.get(keys,'host')
port_value = conf.get(keys,'port')
user_value = conf.get(keys,'user')
password_value = conf.get(keys,'password')
db_value = conf.get(keys,'db')
conn = DBConnect() #类需要初始化
conn.get_connect(host_value,port_value,user_value,password_value,db_value)




