
# 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:

# 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
# ORM、插入、查询语句 
# 本文件为用户数据的插入

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, Date, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime


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

     # 方便对类进行查看 print打印类的时候就会调用这个魔术方法
     def __repr__(self):
        return "User_table(user_id'{self.user_id}', "\
            "user_name={self.user_name}, "\
            "user_age={self.user_age}, "\
            "user_brith={self.user_brith}, "\
            "user_gender={self.user_gender}, "\
            "user_edu={self.user_edu})".format(self=self)


# 实例化一个引擎
dburl='mysql+pymysql://testuser:testpass@192.168.0.106:3306/testdb?charset=utf8mb4'
#                           调试模式
engine=create_engine(dburl, echo=True, encoding='utf-8')

# 创建session 理解为产生一个映射的类
SessionClass = sessionmaker(bind=engine)
# 实例化
session = SessionClass()

# 增加数据
user_demo = User_table(user_name='Timo', user_age= 26,user_brith='1994-05-05', user_gender='male', user_edu='Bachelor')
user_demo2 = User_table(user_name='XiaoMing', user_age=18,user_brith='2001-05-05', user_gender='female', user_edu='highschool')

session.add(user_demo)
session.add(user_demo2)

print (user_demo)

# flush对比commit 最后不会结束事务 最后依然保存连接 不会写入到数据库中
session.flush()
session.commit()