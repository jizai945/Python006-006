# python 连接redis
import redis

redis_server = '127.0.0.1'
redis_pass = '520123'

client = redis.Redis(host=redis_server, password='520123')

print(client.keys())

for key in client.keys():
    print(key.decode())
