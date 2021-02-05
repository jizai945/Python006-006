# 消费者
# 订阅发布
import time
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
channel.queue_declare(queue='task_queue', durable=True)

# 定义一个回调函数来处理消息队列中的消息


def callback(ch, method, properties, body):

    time.sleep(1)
    # 实现如何处理消息
    print(body.decode())
    # 手动发送确认消息
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 如果该消费者的channel上未确认的消息数达到了prefetch_count数，则不向消费者发送消息
channel.basic_qos(prefetch_count=1)

# 消费者使用队列和那个回调函数处理消息
channel.basic_consume('task_queue', callback)

# 开始接收消息，并进入阻塞状态
channel.start_consuming()
