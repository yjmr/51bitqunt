# encoding : urf-8
# author : yj
from pyspark import SparkContext
from pyspark import HiveContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext #sqlconext不支持部分hive语法


def get_spark_session(myApp,memory,parallelism,storageFraction=0.6,shuffleFraction=0.2,core=4):
    # 配置spark context 环境及配置参数，返回spark sc
    sc_conf = SparkConf() # 初始化config
    sc_conf.setMaster("yarn-client") # 客户端执行
    sc_conf.setAppName(myApp)  # 提交的应用程序名称
    sc_conf.set('hive.exec.dynamic.partition', 'true')
    sc_conf.set('hive.exec.dynamic.partition.mode', 'nostrick') # 开启动态分区，非严格模式
    sc_conf.set('spark.sql.autoBroadcastJoinThreshold','-1') #不启用大表关联小表，默认是启用小表数据放内存广播，默认存储大小为10M
    sc_conf.set('hive.exec.max.dynamic.partitions', '100000') #设置每个节点的最大分区数量，默认最大100
    sc_conf.set('hive.exec.max.dynamic.partitions.pernode','100000') #设置所有节点的最大分区数量，默认最大1000
    sc_conf.set('spark.executor.cores',core) #设置core 大小
    sc_conf.set('spark.executor.instances','4') #设置spark执行进程的个数
    sc_conf.set("spark.executor.memory", memory) # 设置执行内存
    sc_conf.set('spark.default.parallelism', parallelism) #设置为num-executors*executor-cores的2-3倍,每个coure执行2-3个任务
    sc_conf.set('spark.storage.memoryFraction',storageFraction) #默认0.6，数据量大设置增大
    sc_conf.set('spark.shuffle.memoryFraction', shuffleFraction) #计算量大，增大设置，默认0.2
    sc_conf.set('spark.logConf', 'True') # 将有效的spark conf 记录为INFO日志中
    print(sc_conf.getAll()) # 打印conf 配置
    sc = SparkContext(conf=sc_conf)
    return sc


def get_spark_sql(sc,query_sql):
    # 通过spark 执行hive sql，返回执行获取的dataframe，并打印行数
    hive_conn =  HiveContext(sc)  #获取session
    dw_dataframe = hive_conn.sql(query_sql)
    dw_data_count = dw_dataframe.count()
    print('>>>>>>>>>>>>>数据返回行数为:{}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'.foramt(dw_data_count))
    return dw_dataframe



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









