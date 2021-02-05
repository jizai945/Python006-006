# 生产者代码
# 订阅发布 有交换机
import pika

MQHost = '127.0.0.1'

# 用户名和密码
# 尽量给不同的业务分配不同的 账号和密码
credentials = pika.PlainCredentials('guest', 'guest')

# 虚拟队列需要指定参数 virtual_host, 如果是默认的可以不填
parameters = pika.ConnectionParameters(host=MQHost,
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)
# 阻塞方法
connection = pika.BlockingConnection(parameters)


# 建立信道
channel = connection.channel()

# 定义交换机
# fanout指的一对多的方式
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = 'send message to fanout'
# exchange指定交换机
# routing_key指定队列名
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message,
                      )


# 关闭与rabbitmq server的连接
connection.close()
