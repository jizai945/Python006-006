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
        value = (1088, "hello")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f'fetch err {e}')

finally:
    #  关闭数据库连接
    db.close()
    print(cursor.rowcount)  # 代表当前成功插入的数据条数
