# redis操作字符串
import redis

redis_server = '127.0.0.1'
redis_pass = '520123'

client = redis.Redis(host=redis_server, password='520123')

# 使用set遇到已存在的key也会覆盖
client.set('key', 'value')
# nx选项遇到已存在的key不会覆盖
client.set('key', 'value1', nx=True)

# 字符串后面追加
client.append('key', 'value4')

client.set('key2', '100')
result2 = client.incr('key2')  # 原有的值做加一的操作
print(result2)

result3 = client.decr('key2')  # 原有值做减一操作
print(result3)

result = client.get('key')
print(result)
print(result.decode())  # 转成字符串类型

# 不要贸然使用 keys * 指令， 会造成redis短暂不响应
