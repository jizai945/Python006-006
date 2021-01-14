# 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:

# 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
# ORM、插入、查询语句 

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base