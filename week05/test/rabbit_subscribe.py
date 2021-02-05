# 消费者代码
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

# 定义一个回调函数来处理消息队列中的消息


def callback(ch, method, properties, body):

    # 手动发送确认消息
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # 实现如何处理消息
    print(body.decode())


# 消费者使用队列和那个回调函数处理消息
channel.basic_consume('direct_demo', on_message_callback=callback)

# 开始接收消息，并进入阻塞状态
channel.start_consuming()
