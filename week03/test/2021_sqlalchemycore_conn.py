# sqlalchemy 连接MySQL 数据库
# pip install sqlalchemy

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;

# echo = True 开启调试 生成环境要去掉
engine = create_engine('mysql+pymysql://testuser:testpass@192.168.0.106:3306/testdb', echo=True)

# 创建元数据 元数据：描述数据的数据
metadata = MetaData(engine)

book_table = Table('book', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20))
    )

author_table = Table('author', metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', None, ForeignKey('book.id')),
    Column('author_name', String(128), nullable=False)
    )    

try:
    metadata.create_all()
except Exception as e:
    print(f'create error{e}')


