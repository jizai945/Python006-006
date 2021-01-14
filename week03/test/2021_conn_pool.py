# 使用连接池

import pymysql
# pip install DBUtils
from dbutils.pooled_db import PooledDB

db_config = {
    "host": "192.168.0.106",
    "port": 3306,
    "user": "testuser", 
    "passwd": "testpass",
    "db" : "testdb",
    "charset": "utf8mb4",
    "maxconnections" : 0 ,      # 连接池允许的最大连接数
    "mincached" : 4,            # 初始化时连接池中中至少创建的空闲的链接，0表示不创建  （作用方便后面连接的速度，空间换时间）
    "maxcached" : 0,            # 连接池中最多闲置的链接，0不限制
    "maxusage" : 5,             # 每个连接最多被重复使用的次数，None表示无限制  （重复使用会导致内存越用越大，需要释放）
    "blocking" : True           # 连接池中如果没有可用连接后是否阻塞等待
                                # True 等待  False 不等待然后报错
}

#  **通过字典的方式传参
spool = PooledDB(pymysql, **db_config)

conn = spool.connection()
cur = conn.cursor() # 游标
SQL = "select * from bookorm;"
cur.execute(SQL)
f = cur.fetchall()
print(f)
cur.close()
conn.close()



