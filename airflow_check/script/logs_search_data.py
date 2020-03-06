from configparser import ConfigParser
import os
import sys
path_abs = os.path.dirname(__file__)
project_home = os.path.dirname(path_abs)
sys.path.append(project_home)
import sourcedb_data
if __name__ == '__main__':

    config_path = r'F:\code\github_files\airflow_check\config\logs_datemark.config'
    if os.path.exists(config_path):
        pass
    else:
        config_path = project_home + '/config/logs_datemark.config'
    logconfig = sourcedb_data.get_config(config_path).sections()
    for table_key in logconfig:
        label = sourcedb_data.get_config(config_path).get(table_key,'label')
        if label == '1':
            table_name = sourcedb_data.get_config(config_path).get(table_key, 'table_name')
            pattern_text = sourcedb_data.get_config(config_path).get(table_key, 'pattern')
            log_path = sourcedb_data.get_config(config_path).get(table_key, 'log_path')
            date_mark = sourcedb_data.search_text(log_path, pattern_text)
            print(table_name, date_mark, sep="|")
        else:
            continue



# print(sourcedb_data.search_text(log_path,pattern))