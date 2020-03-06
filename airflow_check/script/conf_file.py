import os
import sys
from configparser import ConfigParser
path_abs = os.path.dirname(__file__)
print(path_abs)
project_home = os.path.dirname(path_abs)
sys.path.append([project_home])
print(project_home)
table_config_path = project_home + r'/config/data_check.config'
print(table_config_path)

def get_config(path):
    # 读取配置文件方法
    Db_config = ConfigParser()
    Db_config.read(path, encoding='utf-8')
    return Db_config


response = get_config(table_config_path)
print(response.get('test','current_table_query'))
print(response.get('test','type'))