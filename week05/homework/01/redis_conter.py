import redis

redis_server = '127.0.0.1'
redis_pass = '520123'



def conuter(video_id: int):
    client = redis.Redis(host=redis_server, password='520123')
    
    id_str = str(video_id)
    client.set(id_str, '0', nx=True)
    result = client.incr(id_str)  # 原有的值做加一的操作

    return int(result)
    


if __name__=='__main__':
    num = conuter(110)
    print(num)
    print(type(num))
