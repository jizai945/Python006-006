import redis
import time
import string
from functools import wraps

redis_server = '127.0.0.1'
redis_pass = '520123'
one_minute = 1*60


# 次数限制
def send_times(times):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            client2 = redis.Redis(host=redis_server, password='520123')

            str_tele = str(args[0])
            client2.set(str_tele+'times', times, nx=True)
            # client2.set(str_tele+'times', times)
            if int(client2.get(str_tele+'times').decode()) <= 0:
                print('余剩发送次数不足')
            else:
                result = client2.decr(str(args[0])+'times')  # 原有值做减一操作
                client2.close()
                print(f'余剩次数： {result}')
                return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


# 过滤超时的列表消息
def pop_timeout_tick(telephone_number: int):
    tele_str = str(telephone_number)

    tick_list = client.lrange(tele_str, 0, -1)
    for tick in tick_list:
        # print(int(tick.decode()))
        if int(time.time()) - int(tick.decode()) >= one_minute:
            print(f'delet timeout mes :{int(tick.decode())}')
            client.lpop(tele_str)
        else:
            break


@send_times(times=5)
def sendsms(telephone_number: int, content: string, key=None):

    global client
    client = redis.Redis(host=redis_server, password='520123')

    # 弹出超时记录
    pop_timeout_tick(telephone_number)

    # 当前要发送的消息条数
    mes_num = int(len(content)/69) + 1

    # 获取当前还没超时的消息条数
    wait_timeout_mes_num = client.llen(telephone_number)

    if wait_timeout_mes_num+mes_num > 5:
        print('1 分钟内发送次数超过 5 次, 请等待 1 分钟')
    else:
        for i in range(0, mes_num):
            print(content[i*70: (i+1)*70])
            client.rpush(str(telephone_number), str(int(time.time())))

    # # 短信发送逻辑, 作业中可以使用 print 来代替
    # pass
    # # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后
    # pass
    # print("发送成功")


if __name__ == '__main__':

    sendsms(119, "hello")
