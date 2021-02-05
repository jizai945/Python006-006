# redis操作有序集合
import redis

redis_server = '127.0.0.1'
redis_pass = '520123'

client = redis.Redis(host=redis_server, password='520123')

# 添加数据
client.zadd('rank', {'a': 4, 'b': 3, 'c': 1, 'd': 2, 'e': 5})

# 值减操作
client.zincrby('rank', -2, 'e')

# 按照评分 从小到大 查看
print(client.zrangebyscore('rank', 1, 5))
# 从大到小 zrevrank

# 基card 有多少个值
print(client.zcard('rank'))

# 显示评分 从小到大
print(client.zrange('rank', 0, -1, withscores=True))
# 显示评分 从大到小
print(client.zrevrange('rank', 0, -1, withscores=True))
