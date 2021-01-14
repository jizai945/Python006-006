# ORM方式连接MySQL 数据库
# orm方式插入数据到数据库
# # pip install sqlalchemy

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;

Base = declarative_base()

class Book_table(Base):
    __tablename__ = 'bookorm'
    # 变量名就是字段名 整数
    book_id = Column(Integer(), primary_key=True)
    #                   字符串
    book_name = Column(String(50), index=True)

    # 方便对类进行查看 print打印类的时候就会调用这个魔术方法
    def __repr__(self):
        return "Book_table(book_id'{self.book_id}', "\
            "book_name={self.book_name})".format(self=self)

class Author_table(Base):
    __tablename__ = 'authororm'
    #                           是否是主键
    user_id = Column(Integer(), primary_key=True)
    #                             是不是可以为空   是否唯一
    username = Column(String(15), nullable=False, unique=True)
    #                               默认值
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    # Float
    # Decimal
    # Boolean
    # Text
    # autoincrement 自动增长

# 三层结构 -------------- 
# 业务逻辑层
# 持久层
# 数据库层
# ----------------------------------------------------------------


# 实例化一个引擎
dburl='mysql+pymysql://testuser:testpass@192.168.0.106:3306/testdb?charset=utf8mb4'
#                           调试模式
engine=create_engine(dburl, echo=True, encoding='utf-8')

# 创建session 理解为产生一个映射的类
SessionClass = sessionmaker(bind=engine)
# 实例化
session = SessionClass()

# 增加数据
book_demo = Book_table(book_name='肖申克的救赎')
book_demo2 = Book_table(book_name='西游记')
book_demo3 = Book_table(book_name='水浒传')
# author_name = Author_table()
# print(book_demo)
# print(author_name)

session.add(book_demo)
session.add(book_demo2)
session.add(book_demo3)
# flush对比commit 最后不会结束事务 最后依然保存连接 不会写入到数据库中
session.flush()
session.commit()

