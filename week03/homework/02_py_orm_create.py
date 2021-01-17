# 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:

# 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
# ORM、插入、查询语句 
# 本文件为用户数据的创建


import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, Date, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User_table(Base):
     __tablename__ = 'userorm'

     user_id = Column(Integer(), primary_key=True)     # ID
     user_name = Column(String(50), index=True)        # 姓名
     user_age = Column(Integer())                      # 年龄(自动计算)
     user_brith = Column(Date())                       # 生日
     user_gender = Column(String(10))                  # 性别
     user_edu = Column(String(10))                      # 学历
     # 字段创建时间
     created_on = Column(DateTime(), default=datetime.now)
     # 字段更新时间
     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
                

     

# 实例化一个引擎
dburl='mysql+pymysql://testuser:testpass@192.168.0.106:3306/testdb?charset=utf8mb4'
#                           调试模式
engine=create_engine(dburl, echo=True, encoding='utf-8')

Base.metadata.create_all(engine)


