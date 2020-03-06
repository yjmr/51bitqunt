

表的策略配置文件：
    1、表的名称   tablename
    2、key    
    3、源表统一指HDI 或者要策略的当前表 current_table_query   
        支持文件形式(验证策略代码内容太大，支持文件指定) 或者是字符串形式(直接再配置文件写的sql策略)
     需要文件判断方法
    4、对应表 指对应db target 或者是 源表 source_table_query
    5、对应表的查询类型： source_query_type 
            HDI    走spark hive查询
            不是的话，db去查询 jst怎么处理?
    6、对应taskid 
    7、如果是回刷的表，那么就必须先执行回刷的Max_business_date 拿到这个日期 再传给 current_tablename 里
        约定下parse :  transmit_date  
                            在策略代码里面就存在{transmit_date}

    
都在hdi上验证：
    1、回刷传递

    2、非回刷传递，且非读取日志传递

    3、读取日志传递

    要判断是否是日志传递



