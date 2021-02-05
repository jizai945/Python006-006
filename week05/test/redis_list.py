# redis操作列表
import redis

redis_server = '127.0.0.1'
redis_pass = '520123'

client = redis.Redis(host=redis_server, password='520123')

# 插入数据
# client.lpush('list_redis_demo', 'python')
# client.rpush('list_redis_demo', 'java')

# 打印一下列表的长度
print(client.llen('list_redis_demo'))

# 弹出数据
# data = client.lpop('list_redis_demo')
# print(data)
# data = client.rpop('list_redis_demo')
# print(data)

# 查看一定范围的list数据
data = client.lrange('list_redis_demo', 0, -1)
print(data)
