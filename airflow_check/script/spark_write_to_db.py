# encoding : urf-8
# author : yj
from pyspark import SparkContext
from pyspark import HiveContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext #sqlconext不支持部分hive语法

# 20200314 在一个sql context或者hive context中缓存的表，不能再其他的context中使用!!!!
def get_spark_session(myApp,executor,memory,parallelism,storageFraction=0.6,shuffleFraction=0.2,core=4,Broad='-1'):
    # 配置spark context 环境及配置参数，返回spark sc
    sc_conf = SparkConf() # 初始化config
    sc_conf.setMaster("yarn-client") # 客户端执行
    sc_conf.setAppName(myApp)  # 提交的应用程序名称
    sc_conf.set('hive.exec.dynamic.partition', 'true')
    sc_conf.set('hive.exec.dynamic.partition.mode', 'nostrick') # 开启动态分区，非严格模式
    sc_conf.set('spark.sql.autoBroadcastJoinThreshold',Broad) # -1 不启用大表关联小表，默认是启用小表数据放内存广播，默认存储大小为10M
    sc_conf.set('hive.exec.max.dynamic.partitions', '10000') #设置每个节点的最大分区数量，默认最大100
    sc_conf.set('hive.exec.max.dynamic.partitions.pernode','1000000') #设置所有节点的最大分区数量，默认最大1000
    sc_conf.set('spark.executor.cores',core) #设置core 大小
    sc_conf.set('spark.executor.instances',executor) #设置spark执行进程的个数
    sc_conf.set("spark.executor.memory", memory) # 设置执行内存
    sc_conf.set('spark.default.parallelism', parallelism) #设置为num-executors*executor-cores的2-3倍,每个coure执行2-3个任务
    sc_conf.set('spark.storage.memoryFraction',storageFraction) #默认0.6，数据量大设置增大
    sc_conf.set('spark.shuffle.memoryFraction', shuffleFraction) #计算量大，增大设置，默认0.2
    sc_conf.set('spark.logConf', 'True') # 将有效的spark conf 记录为INFO日志中
    print(sc_conf.getAll()) # 打印conf 配置
    sc = SparkContext(conf=sc_conf)
    return sc




def get_spark_sql(sc,query_sql):
    # 通过spark 执行hive sql，返回执行获取的dataframe，和hive context并打印行数
    hive_conn =  HiveContext(sc)  #获取session
    dw_dataframe = hive_conn.sql(query_sql)
    dw_data_count = dw_dataframe.count()
    print('>>>>>>>>>>>>>数据返回行数为:{}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'.foramt(dw_data_count))
    return dw_dataframe,hive_conn




def get_write_db():
    #写入数据到db
    pass

def get_table_cache(sc,cache_table):
    #缓存小表在内存中，并且开启广播变量
    hive_conn =  HiveContext(sc)
    if cache_table == 'None':
        pass
    else:
        new_cache_table = cache_table + '_cache'
        hive_conn.sql('cache table {} select * from {} '.foramt(new_cache_table,cache_table))
        print("缓存表:{}，缓存后为{}".format(cache_table, new_cache_table))
    return sc,hive_conn



def get_config(path):
    # 读取配置文件方法
    Db_config = ConfigParser()
    Db_config.read(path,encoding='utf-8')
    return Db_config


def get_write_table(sc,df,table_name,write_table_type,partition_type)
    #将dataframe写入表
    if write_table_type == 'append':
        if partition_type == 'None':
            #写入分区表
            pass
        else:
            #写入非分区表
            pass
    else:
        if partition_type == 'None':
            #全量写入分区表
            pass
        else:
            #全量写入非分区表
            pass
    print("写入{}完成".format(table_name))


def pub_write_to_data():
    # 要传入配置文件路径，配置的key就ok了
    pass
def get_write_db(dw_dataframe,db_name,db_type,table_name,truncate_value="True"):
    # pyspark写入db
    if db_type = 'mysql':
        dw_dataframe.write.mode("append").format("jdbc")\
            .option('url':"jdbc:mysql://ip地址:端口号/库名称" + "?rewriteBatchedStatements=true")\
            .option("dbtable",table_name)\
            .option("driver", "com.mysql.cj.jdbc.Driver")\
            .option("user","用户名") \
            .option("password","密码")\
            # 批量插入，写入1W行，默认是1000
            .option("batchsize",10000)\
            # 默认写入清空表
            .option("truncate",truncate_value).save()
    else:
        dw_dataframe.write.mode("append").format("jdbc") \
            .option("driver" ,"com.microsoft.sqlserver.jdbc.SQLServerDriver") \
            #开启批量插入模式
            .option('url':"jdbc:mysql://ip地址:端口号/库名称" + "?rewriteBatchedStatements=true") \
            .option("dbtable",table_name) \
            .option("user","用户名") \
            .option("password","密码") \
            #批量插入，写入1W行，默认是1000
            .option("batchsize",10000) \
            #默认写入清空表
            .option("truncate",truncate_value).save()










