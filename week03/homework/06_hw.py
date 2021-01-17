# .张三给李四通过网银转账 100 极客币，现有数据库中三张表：

# 一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
# 第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

# 请合理设计三张表的字段类型和表结构；
# 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, Date, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()


# 表格1 用户ID和用户名
class User_table(Base):
    __tablename__ = 'user_IDorm'
    #                                               唯一
    user_id = Column(Integer(), primary_key=True, unique=True )     # ID
    #                                           
    user_name = Column(String(50), index=True)        # 姓名

# 表格2  用户ID和用户资产
class Momey_table(Base):
    __tablename__ = 'user_Moneyorm'

    user_id = Column(Integer(), primary_key=True, unique=True )     # ID
    user_money = Column(Integer())        # 姓名     

# 表格3  转账时间，转账 id，被转账 id，转账金额
class Details_table(Base):
    __tablename__ = 'user_Detailsorm'

    from_id = Column(Integer(), primary_key=True )     # 转账ID
    to_id = Column(Integer(), primary_key=True )     # 被转账ID
    money = Column(Integer())        # 金额  
    # 字段更新时间
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# 创建表
def create_tables():
    Base.metadata.create_all(engine)

# 添加用户
def add_user(name, money):
    if not (isinstance (name, str)): 
        print(f'name err {type(name)}')
        return

    if not (isinstance (money, int)):
        print(f'money err {type(money)}')
        return


    # 创建session 理解为产生一个映射的类
    SessionClass = sessionmaker(bind=engine)
    # 实例化
    session = SessionClass()

    # 添加用户表
    user_add = User_table(user_name=name)
    session.add(user_add)
    # flush对比commit 最后不会结束事务 最后依然保存连接 不会写入到数据库中
    session.flush()

    # 查询创建之后的用户ID
    print('.............')
    res = session.query(User_table).filter(User_table.user_name == name).first()
    print(res.user_id)
        
    # 添加资产表
    money_add = Momey_table(user_id = res.user_id, user_money = money)
    session.add(money_add)
    # flush对比commit 最后不会结束事务 最后依然保存连接 不会写入到数据库中
    session.flush()

    # 提交
    session.commit()


# 交易函数
def transfer(from_name, to_name, money):
    if not (isinstance (from_name, str)): 
        print(f'name err {type(from_id)}')
        return

    if not (isinstance (to_name, str)):
        print(f'money err {type(to_id)}')
        return 

    if not (isinstance (money, int)):
        print(f'money err {type(to_id)}')
        return     

    # 创建session 理解为产生一个映射的类
    SessionClass = sessionmaker(bind=engine)
    # 实例化
    session = SessionClass()

    # 查询 id
    try :
        tables1_from = session.query(User_table).filter(User_table.user_name == from_name).first()
        tables1_to = session.query(User_table).filter(User_table.user_name == to_name).first()
        print(tables1_from.user_id)
        print(tables1_to.user_id)

    except Exception as e:
        print(f'查询id错误 {e}')
        return

    # 判断余额是否满足交易
    try :
        tables2_from = session.query(Momey_table).filter(Momey_table.user_id == tables1_from.user_id).first()
        tables2_to = session.query(Momey_table).filter(Momey_table.user_id == tables1_to.user_id).first()
        print(f'交易前转账者余额: {tables2_from.user_money}')
        print(f'交易前被转账者余额: {tables2_to.user_money}')
    except Exception as e:
        print(f'查询余额错误 {e}')
        return

    if (tables2_from.user_money < money):    
        print('余额不足')
        return

    tables2_from.user_money, tables2_to.user_money = tables2_from.user_money-money, tables2_to.user_money+money
    print(f'交易后转账者余额: {tables2_from.user_money}')
    print(f'交易后被转账者余额: {tables2_to.user_money}')

    # 更新表交易记录
    details = Details_table(from_id=tables1_from.user_id, to_id=tables1_to.user_id, money=money)
    session.add(details)
    # 更新表余额
    query = session.query(Momey_table)
    query = query.filter(Momey_table.user_id == tables1_from.user_id)
    query.update({Momey_table.user_money: tables2_from.user_money})
    new_query = query.first()
    print(new_query.user_money)
    query = session.query(Momey_table)
    query = query.filter(Momey_table.user_id == tables1_to.user_id)
    query.update({Momey_table.user_money: tables2_to.user_money})
    new_query = query.first()
    print(new_query.user_money)

    session.commit()

if __name__ == '__main__':

    # 实例化一个引擎
    dburl='mysql+pymysql://testuser:testpass@192.168.0.106:3306/testdb?charset=utf8mb4'
    #                           调试模式
    engine=create_engine(dburl, echo=True, encoding='utf-8')

    create_tables()

    # 添加用户
    # add_user('Timo', 1000)
    # add_user('张三', 1000)
    # add_user('李四', 1000)

    # 交易测试
    transfer('张三', '李四', 9999)
    transfer('李四', '张三', 200)
