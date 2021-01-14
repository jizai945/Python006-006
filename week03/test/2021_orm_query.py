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

# author_name = Author_table()
# print(book_demo)
# print(author_name)

# 不加all方法不行， 不加all只是查询了但是没有筛选符合查询的结果
# 查询
result = session.query(Book_table).all()
print(result)

result = session.query(Book_table).first()
print(result)

for result in session.query(Book_table):
    print(result)

# first()   只会选择第一个
# one()     查询所有行，如果返回结果不是单独的一个的时候就会抛出异常
# scalar() 返回第一个结果的第一个元素，如果没有就返回None,多于一个结果也会引发异常

# 指定查询的列数
session.query(Book_table.book_name).first()

# 排序
for result in session.query(Book_table.book_id, Book_table.book_name).order_by(Book_table.book_id):
    print(result)
# 逆序
from sqlalchemy import desc
for result in session.query(Book_table.book_id, Book_table.book_name).order_by(desc(Book_table.book_id)):
    print(result)

# 限制 返回条数
query = session.query(Book_table).order_by(desc(Book_table.book_id)).limit(3)
print([result.book_name for result in query])

from sqlalchemy import func
# 统计行数
result = session.query(func.count(Book_table.book_name)).first()
print(result)

# 过滤
print(session.query(Book_table).filter(Book_table.book_id < 20).first() )
# 以下举filter例
# filter(Book_table.book_id > 10, Book_table.book_id < 20)
# from sqlalchemy import and_, or_, not_
# filter(
#     or_(
#         Book_table.book_id.between(0, 5)
#         Book_table.book_name.contains('肖申克的救赎 ')
#     )
# )

session.commit()

