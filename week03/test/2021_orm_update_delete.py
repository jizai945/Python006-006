# ORM方式连接MySQL 数据库
# orm方式查询数据
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

# 更新
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 1)
query.update({Book_table.book_name: '芜湖'})
new_book = query.first()
print(new_book.book_name)

# 删除 
# 比较危险 无法恢复只能靠数据库备份恢复
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 3)
# 删除一行
# session.delete(query.one())   # 第一种删除方法
# 或者用这种方法删除
query.delete()
print(query.first())

session.commit()
