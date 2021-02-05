**作业二：**在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次，请基于 Python 和 redis 实现如下的短信发送接口：
已知有如下函数：

复制代码

```
def sendsms(telephone_number: int, content: string, key=None)：
    # 短信发送逻辑, 作业中可以使用 print 来代替
    pass
    # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后
    pass
    print("发送成功")
```

**期望执行结果：**

sendsms(12345654321, content=“hello”) # 发送成功
sendsms(12345654321, content=“hello”) # 发送成功
…
sendsms(88887777666, content=“hello”) # 发送成功
sendsms(12345654321, content=“hello”) # 1 分钟内发送次数超过 5 次, 请等待 1 分钟
sendsms(88887777666, content=“hello”) # 发送成功

**选做：**
1.content 为短信内容，超过 70 个字自动拆分成两条发送
\2. 为 sendsms() 函数增加装饰器 send_times()，通过装饰器方式实现限制手机号最多发送次数，如：

复制代码

```
@send_times(times=5)
sendsms()
```