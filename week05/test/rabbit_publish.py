# 生产者代码
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

# 声明消息队列
# 生产者和消费者都可以声明，尽量两边都声明，防止报错，如不存在自动创建
# durable=True 队列持久化 是否保存到硬盘上
channel.queue_declare(queue='direct_demo', durable=False)

# exchange指定交换机
# routing_key指定队列名
channel.basic_publish(exchange='', routing_key='direct_demo',
                    body='send message to rabbitmq')

# 关闭与rabbitmq server的连接
connection.close()