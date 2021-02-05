# redis操作集合
import redis

redis_server = '127.0.0.1'
redis_pass = '520123'

client = redis.Redis(host=redis_server, password='520123')

# 第一次添加打印值为1 后面添加返回值为0
print(client.sadd('redis_set_demo', 'new_data'))

# 随机弹出一个数据
# client.spop()

# 查看所有值
print(client.smembers('redis_set_demo'))

# 集合的交集
client.sinter('set_a', 'set_b')

# 集合的并集
client.sunion('set_a', 'set_b')

# 集合的差集
client.sdiff('set_a', 'set_b')
