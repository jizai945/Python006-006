# WEEK03笔记



## MySQL安装

企业级MySQL部署再Linux操作系统上，需要注意的重点:

+   注意操作系统的平台(32位、64位)
+   注意安装MySQL的版本（MySQL企业版(付费)、社区版、MariaDB）
+   注意安装后避免yum自动更新
+   注意数据库的安全性



访问 http://dev.mysql.com/下载社区版

5.7.32GA

```ubuntu
# 查看有没有安装MySQL：
sudo dpkg -l | grep mysql

# 安装MySQL：
sudo apt install mysql-server

# 安装完成之后可以使用如下命令来检查是否安装成功：
sudo netstat -tap | grep mysql
# 通过上述命令检查之后，如果看到有 mysql 的socket处于 LISTEN 状态则表示安装成功。

# 启动mysql服务
sudo systemctl start mysql.service

# 登录mysql数据库可以通过如下命令：
mysql -u root -p

# 查看数据库版本
mysql -V


```

==在vim 输入"/bind-address" 找到bind-address = 127.0.0.1,在前面加个#注释掉，保存退出；==

```mysql
# 修改密码
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';

# 查看当前密码强度要求
show variables like "%password%";

# 可以设置对应项密码强度和规整

```



## 正确使用MySQL字符集

==一定要注意字符集问题，否则改起来很困难==

==注意：MsSQL中的utf8不是UTF-8字符集==

```mysql
# 查看字符集
show variables like '%character%';

# 查看校对规则
show variables like 'collation_%';
```



字符集意思

```
ke+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8mb4                    |
| character_set_connection | utf8mb4                    |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | utf8mb4                    |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+

character_set_client:客户端来源的时候使用的字符集
character_set_connection：连接层面的字符集
character_set_database：当前选中的数据库的字符集
character_set_filesystem：连接系统
character_set_results：显示的查询结果
character_set_server：服务端的字符集
character_set_system：系统元数据

mysql> show variables like 'collation_%'
    -> ;
+----------------------+--------------------+
| Variable_name        | Value              |
+----------------------+--------------------+
| collation_connection | utf8mb4_unicode_ci |
| collation_database   | utf8mb4_unicode_ci |
| collation_server     | utf8mb4_unicode_ci |
+----------------------+--------------------+
ci大小写不敏感
cs大小写敏感


```



utf8最多占用三字节

utf8mb4占用4字节

```ubuntu
# 修改mysql字符集配置文件
sudo vim /etc/mysql/my.cnf

在文件中添加下面项
[client]
default_character_set = utf8mb4

[mysql]
default_character_set = utf8mb4

[mysqld]
interactive_timeout= 28800
wait_timeout= 28800
max_connections=1000
character_set_server = utf8mb4
init_connect = 'SET NAMES utf8mb4'
character_set_client_handshake = FALSE
collation_server = utf8mb4_unicode_ci
```



## Python连接MySQL的方法

同一概念：

​	其他语言：连接器、绑定、binding

​	Python语言： Python Database API、DB-API



==注意：MySQLdb是Python2的包，适用于MySQL5.5和Python2.7==



Python3 连接MySQL:

+   Python3安装的MySQLdb包叫做mysqlclient,加载的依然是MySQLdb
+   pip install mysqlclient
+   import MySQLdb

其他DB-API：

+   pip install pymysql 								# 流行度最高
+   pip install mysql-connector-python 	# MySQL官方

使用ORM：

+   pip install sqlalchemy



什么是ORM：（对象 关系 映射）

对底层的sql更高级的一个封装



偏向于面向过程：

```python
# PyMYSQL连接 MySQL数据库


import pymysql

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;
#   连接的服务器    连接的远程用户名   密码     连接的数据库的名
db = pymysql.connect(host="192.168.0.106", port=3306, user="testuser", password="testpass", database="testdb",charset='utf8mb4')

try:
    # 使用cursor（）方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute() 方法执行 SQL 查询
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f'fetch err {e}')

finally:
    #  关闭数据库连接
    db.close()

print(f'Database version : {result}')


```



偏向于面向对象：

```python
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

```

去mysql数据库中可以看到刚刚创建的表

```
mysql> use testdb;
mysql> show tables;
```



使用orm的方式连接数据库

```python
# ORM方式连接MySQL 数据库
# # pip install sqlalchemy

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;

Base = declarative_base()

class book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)


    # book_table = Table('book', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('name', String(20))
    #     )

# 定义一个更多的列属性的类
from datetime import datetime
from sqlalchemy import DateTime

class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# 实例化一个引擎
dburl='mysql+pymysql://testuser:testpass@192.168.0.106:3306/testdb?charset=utf8mb4'
engine=create_engine(dburl, echo=True, encoding='utf-8')

Base.metadata.create_all(engine)


```



## 必须掌握的SQL知识



SQL语言功能划分：

+   DQL: Data Query Language，数据查询语言，开发工程师学习的终点
+   DDL:Data Definition Language,数据定义语言，操作库和表结构
+   DML:Data Manipulation Language,数据操作语言，操作表中记录
+   DCL:Data Control Language, 数据控制语言，安全和访问权限控制



```sql
CREATE TABLE 'book'( 
    'book_id'int(11) NOT NULL AUTO_INCREMENT,
    'book_name'varchar(255) , 
    PRIMARY KEY ('book_id') 
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci;
```



==如上创建表要注意哪些问题?==

1.   创建表之前判断表是否存在
2.   一般创建字段使用反引号，以区别不同于MySQL保留字段
3.   指定字符集
4.   创建表的个数尽量越少越好
5.  联合主键当中的字段尽量越少越好
6.  外键要在应用层解决(性能考虑)



==查询数据要注意哪些问题==

SELECT查询时关键字的顺序

==SELECT...FROM...WHERE...GROUP BY...HAVING...ORDER BY...LIMIT==

注意： 1. 生成环境下因为列数相对较多，一般禁用 SELECT *

​			2. WHERE字段为避免全表扫描，一般需要增加索引



```sql
CREATE TABLE `book`( 
    `book_id` int(11) NOT NULL AUTO_INCREMENT, 			    		
    `type_id` int(11) NOT NULL,
    `book_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    PRIMARY KEY ('book_id')  USING BTREE,
    ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci;

														# 执行顺序
SELECT DISTINCT book_id, book_name, count(*) as number  # 5
FROM book JOIN author ON book.sn_id = author.sn_id      # 1
WHERE page > 500                                        # 2 
GROUP BY book.book_id                                   # 3
HAVING number > 10                                      # 4
ORDER BY number                                         # 6
LIMIT 5                                                 # 7
```



## 使用聚合函数汇总数据

### SQL函数有哪些？

算术函数、字符串函数、日期函数、转换函数、聚合函数



### 聚合函数

+   COUNT()		行数
+   MAX()             最大值
+   MIN()              最小值
+   SUM()             求和
+   AVG()              平均值

注意：聚合函数忽略空行



## 多表操作用到的子查询和join关键字解析

 

什么是子查询？

需要从查询结果集中再次查询，才能得到想要的结果



子查询需要关注的问题？

+   关联子查询与非关联子查询区别
+   何时使用IN，何时使用EXISTS.



常见的连接(JOIN)有哪些？

+   自然连接
+   ON连接
+   USING连接
+   外连接
    +   左外连接
    +   右外连接
    +   全外连接（MySQL不支持）



## 事务的特性和隔离级别



什么是事务？

要么全执行，要么不执行



事务的特性 -- ACID

+   A:原子性	Atomicity
+   C:一致性    Consistency
+   I:隔离性    Isolation
+   D:持久性    Durability



事务的隔离级别

==读未提交==：允许读到未提交的数据

==读已提交==：只能读到已经提交的内容

==可重复性==：同一事物在相同查询条件下两次查询得到的数据结果一致

==可串行化==：事务进行串行化，但是牺牲了并发性能

级别越高越影响并发性能，但是安全性越高



查看是否自动提交

```sql
mysql> show variables like 'autocommit';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| autocommit    | ON    |
+---------------+-------+
1 row in set (0.16 sec)

# 关闭自动提交
mysql>set autocommit = 0;


```





## PyMySQL的增删改查操作演示



python插入数据

```python
# PyMYSQL连接 MySQL数据库
# 数据插入

import pymysql

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;

#   连接的服务器    连接的远程用户名   密码     连接的数据库的名
db = pymysql.connect(host="192.168.0.106", port=3306, user="testuser", password="testpass", database="testdb",charset='utf8mb4')

try:
    # 使用cursor（）方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        # %s是占位符 无论是字符串还是数字都用%s
        sql = '''INSERT INTO book (id, name) VALUES (%s, %s)'''
        value = (1001, "活着")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f'fetch err {e}')

finally:
    #  关闭数据库连接
    db.close()
    print(cursor.rowcount)  # 代表当前成功插入的数据条数

```



查看插入的数据

```mysql
show databases;
use testdb;
show tables;
desc book;
select * from book;
```



python数据的查询

```python
# PyMYSQL连接 MySQL数据库
# 数据查询

import pymysql

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;

#   连接的服务器    连接的远程用户名   密码     连接的数据库的名
db = pymysql.connect(host="192.168.0.106", port=3306, user="testuser", password="testpass", database="testdb",charset='utf8mb4')

try:
    # 使用cursor（）方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SELECT name FROM book'''
        cursor.execute(sql)
        books = cursor.fetchall()	 # 取出数据中所有匹配的行
        # fetchone() 方法是取出一行
        # books = cursor.fetchone();
        for book in books:	# 取出的数据是元组
            print(book)
        
    db.commit()

except Exception as e:
    print(f'fetch err {e}')

finally:
    #  关闭数据库连接
    db.close()
    print(cursor.rowcount)


```



python数据的更新修改

```python
# PyMYSQL连接 MySQL数据库
# 数据修改更新

import pymysql

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;

#   连接的服务器    连接的远程用户名   密码     连接的数据库的名
db = pymysql.connect(host="192.168.0.106", port=3306, user="testuser", password="testpass", database="testdb",charset='utf8mb4')

try:
    # 使用cursor（）方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        #更新不成功
        # sql = 'UPDATE book SET name = %s WHERE id = %s'
        # value = ("活着", 1011) 

        # 顺序不能颠倒
        sql = 'UPDATE book SET id = %s WHERE name = %s'
        value = (1011, "活着") 

        cursor.execute(sql, value)      
    db.commit()

except Exception as e:
    print(f'fetch err {e}')

finally:
    #  关闭数据库连接
    db.close()
    print(cursor.rowcount)


```



python数据的删除

```python
# PyMYSQL连接 MySQL数据库
# 数据修改更新

import pymysql

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;

#   连接的服务器    连接的远程用户名   密码     连接的数据库的名
db = pymysql.connect(host="192.168.0.106", port=3306, user="testuser", password="testpass", database="testdb",charset='utf8mb4')

try:
    # 使用cursor（）方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = 'DELETE FROM book WHERE name = %s'
        value = ("活着")
        cursor.execute(sql, value)      
    db.commit()

except Exception as e:
    print(f'fetch err {e}')

finally:
    #  关闭数据库连接
    db.close()
    print(cursor.rowcount)


```





## 多文件插入&如何设计一个良好的数据库连接配置文件



大量数据插入的时候不要使用循环会影响效率，最好在python中使用executemany的方法



```python
# PyMYSQL连接 MySQL数据库
# 数据多行插入

import pymysql

# 打开数据库连接
# mysql> create database testdb;
#                                           用户名   %通配符匹配所有远程用户   密码
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
# FLUSH PRIVILEGES;

#   连接的服务器    连接的远程用户名   密码     连接的数据库的名
db = pymysql.connect(host="192.168.0.106", port=3306, user="testuser", password="testpass", database="testdb",charset='utf8mb4')

try:
    # 使用cursor（）方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        # %s是占位符 无论是字符串还是数字都用%s
        sql = '''INSERT INTO book (id, name) VALUES (%s, %s)'''
        value = (
            (1006, "斗破苍穹"),
            (1007, "芜湖起飞")，
        )
        
        cursor.executemany(sql, value)
    db.commit()

except Exception as e:
    print(f'fetch err {e}')

finally:
    #  关闭数据库连接
    db.close()
    print(cursor.rowcount)  # 代表当前成功插入的数据条数

```



保存配置文件的一个方式： ini	yaml	json



读取ini配置文件:

dbconfig.py

```python
from configparser import ConfigParser

def read_db_config(filename = 'config.ini', section = 'mysql'):
    ''' Read database configuration file and return a dictionary
    :param filename: name of the configuration file
    :param section: name of the configuration
    :return: a dictionary of database paramters 
    '''

    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    print(items)    # 列表套元组的格式
    return dict(items)  # 强转成字典的形式

if __name__ == '__main__':
    print(read_db_config())
```



然后通过调用读取配置文件的模块实现连接数据库

dbconnect.py

```python
import pymysql
from dbconfig import read_db_config

dbserver = read_db_config()

db = pymysql.connect(**dbserver)

try:
    # 使用cursor（）方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute() 方法执行 SQL 查询
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f'fetch err {e}')

finally:
    #  关闭数据库连接
    db.close()

print(f'Database version : {result}')


```



## 使用SQLAchemy插入数据到MySQL数据库



插入数据：

```python
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
book_demo3 = Book_table(book_name='hello')
# author_name = Author_table()
# print(book_demo)
# print(author_name)

session.add(book_demo)
session.add(book_demo2)
session.add(book_demo3)
# flush对比commit 最后不会结束事务 最后依然保存连接 不会写入到数据库中
session.flush()
session.commit()


```



查询数据

```python
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


```



更新和删除

```python
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

```



##  使用连接池优化&数据库建立连接的过程



之前的方式操作数据库之前都要先去连接，并发的时候可能会出问题



```python
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




```



## 优化数据库

权衡利弊



### 调优的原则：

+   调优不是万能的，升级硬件往往比调优效果更明显
+   调优的效果会虽则次数增加，逐渐递减
+   应该有体系的调整，而不是发现一个参数可以改动就试一试