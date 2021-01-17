# homework1



## 将修改字符集的配置项、验证字符集的 SQL 语句


1.  查看字符集

mysql> show variables like '%character%';

2.  查看校对规则

mysql> show variables like 'collation_%';

3.   修改字符集的方法

    ```
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

    



## 将增加远程用户的 SQL 语句

```sql
#                              数据库       用户名   %通配符匹配所有远程用户   密码
mysql> GRANT ALL PRIVILEGES ON *.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
# 立即生效
FLUSH PRIVILEGES;
```

