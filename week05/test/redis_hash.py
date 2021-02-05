# redis操作哈希
import redis

redis_server = '127.0.0.1'
redis_pass = '520123'

client = redis.Redis(host=redis_server, password='520123')

# 添加
# client.hset('vip_user', '1001', 1)
# client.hset('vip_user', '1002', 1)

# # 删除
# client.hdel('vip_user', '1002')

# # 检查是否存在
# print(client.hexists('vip_user', '1002'))

# # 添加多个键值对
# client.hmset('vip_user', {'1003': 1, '1004': 1})

# hkeys hget hmget hgetall
# hkeys用于获取所有的字段名
# hget获取一个字段
# hmget获取多个字段
# 获取一个哈希表中的所有字段
# 返回值都是bytes，需要decode转换类型
field = client.hkeys('vip_user')
print(field)
print(client.hget('vip_user', '1001'))
print(client.hgetall('vip_user'))
