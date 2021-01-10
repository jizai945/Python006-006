# WEEK02学习笔记



## TCP/IP协议与Socket编程的关系



### OSI参考模型与TCP/IP模型



|      | OSI参考模型 | TCP/IP模型 |      |
| ---- | ----------- | ---------- | ---- |
| 7    | 应用层      | 应用层     | 4    |
| 6    | 表示层      | 应用层     | 4    |
| 5    | 会话层      | 应用层     | 4    |
| 4    | 传输层      | 传输层     | 3    |
| 3    | 网络层      | 网络层     | 2    |
| 2    | 数据链路层  | 物理接口层 | 1    |
| 1    | 物理层      | 物理接口层 | 1    |



### Socket编程

​	TCP/UDP



![socket1](.\socket1.png)



![socket2](.\socket2.png)





#### Socket API

-   socket()
-   bind()
-   listen()
-   accept()
-   recv()
-   send()
-   close()



#### socket客户端

```python
# requests包很好的帮我们把socket的请求封装了
import requests

r = requests.get('http://www.httpbin.org')
print(r.status_code)
print(r.headers)
print(r.text)
```

也可通过下面代码去请求

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# debug
print(f"s1 : {s}")

s.connect(('www.httpbin.org', 80))

#debug
print(f"s2 : {s}")

# http头部信息
s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n')

buffer = []

while True:
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break

s.close()

response = b''.join(buffer)

header, html = response.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

with open('index.html', 'wb') as f:
    f.write(html)

```



#### echo server

客户端代码

```python
import socket

HOST = 'localhost'
PORT = 10000

def echo_client():
    '''Echo Server 的Client端'''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        #  接受用户输入数据并发送服务端
        data = input('input > ')

        # 设定推出条件
        if data == 'exit':
            break

        # 发送数据到服务端
        s.sendall(data.encode())

        # 接受服务端数据
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))

    s.close()


if __name__=='__main__':
    echo_client()

```



服务端代码

```python
import socket

HOST = 'localhost'
PORT = 10000

def echo_server():
    ''' Echo Server的Server端 '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将对象s绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 只接受一个连接
    s.listen(1)

    while True:
        # accept表示接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

        conn.close()    

    s.close()


if __name__=='__main__':
    echo_server()


```



### 前端基础



| 客户端                                   |                                                             | 服务端                                |
| ---------------------------------------- | ----------------------------------------------------------- | ------------------------------------- |
| HTTP                                     | -----body header----                                        | HTTP                                  |
| TCP                                      | -----IP 和 端口----                                         | TCP                                   |
| 网络层                                   |                                                             | 网络层                                |
| 数据链路层                               |                                                             | 数据链路层                            |
| 物理层                                   |                                                             | 物理层                                |
| \|                                       |                                                             | \|                                    |
| \|______________________________________ | __________________internet_________________________________ | ___________________________________\| |



f12 查看网页源码

w3c标准

ajax异步请求更新网页数据



### HTTP协议和浏览器的关系

请求的时候注意 Headers

Requeset URL:请求的网址

Requeset Method:请求的方式 GET/POST

status Code: 请求返回结果

Request Headers: 具体的请求头

​	--> **Cookie**:带着用户名密码的验证信息请求

​	-->**User-Agent**：告诉服务器现在客户端的浏览器方式，有反爬虫的作用



HTTP状态码(响应代码)

| HTTP响应代码 |            |
| ------------ | ---------- |
| 1xx          | 信息响应   |
| 2xx          | 成功响应   |
| 3xx          | 重定向     |
| 4xx          | 客户端响应 |
| 5xx          | 服务端响应 |



html常见的标签 

--> span 文字

--> a 链接

--> img 图片



### requests库



```python
# 使用requests库获取豆瓣影评

import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

print(response.text)
print(f'返回码是:{response.status_code}')

```



### 异常捕获

with open 比直接open好用

比如运行到某一步突然断网了

```python
# 使用try

x = 0
try:
    100/x
    print('123')
except Exception as e:
    print(e)
```



Traceback函数追踪问题

异常处理机制的原理：

+   异常也是一个类
+   异常捕获过程：
    1.   ==异常类把错误消息打包到一个对象==
    2.   ==然后该对象会自动查找到调用栈==
    3.   ==只用运行系统找到明确声明如何处理这些类异常的位置==
+   所有异常继承自 BaseException
+   Traceback显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的



==在程序运行中，在捕获的代码段中捕获到了异常，则异常后面的代码就不会运行==



```python
# 自定义异常类

class UserInputError(Exception):
    # 类的初始化
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):
        return self.errorinfo+'123'


userinput = 'a'

try:
    if(not userinput.isdigit()):
        raise UserInputError('用户输入错误')

except UserInputError as ue:
    print(ue)

finally:
    del userinput


```



==当使用print输出对象的时候，只要类自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据==



美化异常输出的第三方库  pretty_errors



当with语句在开始运行时，会在上下文管理器对象上调用 __ enter__ 方法。with语句运行结束后，会在上下文管理器对象上调用 __ exit__ 方法

__ call__主要实现的是将类的对象当作函数直接调用

```python
class Open():
    def __enter__(self):
        print('open')
    
    def __exit__(self, type, value, traceback):
        print('close')
	# 主要实现的是将类的对象当作函数直接调用
    def __call__(self):
        print('666')
        pass

with Open() as f:
    pass

test = Open()
test()

```



### 增加程序健壮性



抓取豆瓣网页并写入到本地文件中



```python
# 使用requests库获取豆瓣影评
import requests
from pathlib import *
import sys
# PEP-8
# Google Python 风格指引

# 浏览器版本
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

try:
    response = requests.get(myurl, headers=header, timeout=10)
except requests.exceptions.ConnectTimeout as e:
    print(f'requests 库超时{e}')
    sys.exit(1)

print(response.text)
print(f'返回码是:{response.status_code}')

# 将网页内容改为存入文件

# 获得python脚本的绝对路径
p = Path(__file__)
print(p)
pyfile_path = p.resolve().parent
# 建立新的目录html
html_path = pyfile_path.joinpath('html')

# 判断目录是否存在
if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')

# 上下文管理器
try:
    with open(page, 'w', encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print(f'文件无法打卡,{e}')
except IOError as e:
    print(f'读写文件出错, {e}')
except Exception as e:
    print(e)


```



### 深入了解HTTP协议

get不适合传递密码，参数在url里面



```python
import requests

r = requests.get('http://www.httpbin.org')
r
r.text
r.url

payload = {'key1':'value1', 'key2':['value2', 'value3']}
# 通过这种方式给get请求添加参数
r = requests.get('http://www.httpbin.org', params=payload)
r.url
```



cookie:服务器记录你当前的登陆或者访问的信息，丢给你的浏览器。

requests模拟登录的信息去访问需要带上cookie

Referer：表示从哪个页面访问过来

User-Agent：浏览器的类型



### 深入了解POST方式和cookie



```python
# http 协议的GET方法
import requests
r = requests.get('https://github.com')
r.status_code
r.headers['content-type']

# r.text
r.encoding
# r.json()

# http协议的POST方法
import requests
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.json()

```



```python
import requests

# 在同一个Session 实例发出的所有请求之间保持cookie
s = requests.Session()

s.get('htttp://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('htttp://httpbin.org/cookies')

print(r.text)

# 会话可以使用上下文管理器
with requests.Session() as s:
    s.get('htttp://httpbin.org/cookies/set/sessioncookie/123456789')
```



模拟登录，登录的信息cookie临时存储在会话中，使用这个会话进行下一次请求

```python
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# 会话对象 在同一个Session实例发出的所有请求之间保持cookie
# 期间使用urllib3 的 connection pooling 功能
# 向同一主机发送多个请求，底层的TCP连接将会重用，从而带来显著的性能提升
login_url = 'https://accounts.douban.com/passport/login'
form_data = {
    'ck':'', 
    'remember': 'false',
    'name': '13580789907',
    'password': '6666',
    'ticket':''
}

response = s.post(login_url, data = form_data, headers = headers)
print(response.text)


# 登录后可以进行后续的请求
url2 = 'https://accounts.douban.com/passport/setting'

response2 = s.get(url2, headers = headers)

with open('profile.html', 'w+', encoding='utf-8') as f:
    f.write(response2.text)

```



###  使用XPath匹配网页内容&实现翻页功能



获取豆瓣前250电影名字和链接

zip方法可以把两个列表进行连接

```python
# 翻页的处理
import requests
from lxml import etree
from time import sleep
# 控制请求的频率 引入了time模块

# 使用了def定义函数 myurl是函数的参数
def get_url_name(myurl):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    headers = {'User-Agent': ua}
    response = requests.get(myurl, headers=headers)

    selector = etree.HTML(response.text)
    # 电影名称列表
    film_name = selector.xpath('//div[@class="hd"]/a/span[1]/text()')

    # 电影连接列表
    film_link = selector.xpath('//div[@class="hd"]/a/@href')

    #遍历对应关系字典
    film_info = dict(zip(film_name, film_link))
    for i in film_info:
        print(f'电影名称: {i} \t\t 电影链接: {film_info[i]}')

if __name__ == '__main__':
    # 生成包含所有页面的元组
    urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))
    
    print(urls)

    for page in urls:
        get_url_name(page)
        sleep(5)
```





### 自顶向下设计

什么是自顶向下设计?

+   从整体分析一个比较复杂的大问题
+   分析方法可以服用
+   拆分到你能解决的范畴



实战将爬虫代码拆解模拟Scrapy框架



![img](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fjiantuku-liwenbin.oss-cn-shanghai.aliyuncs.com%2F18-11-13%2F84645295.jpg&refer=http%3A%2F%2Fjiantuku-liwenbin.oss-cn-shanghai.aliyuncs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1612780778&t=0b4234b796090178d6fcc1a36d61007a)

+   什么是Scrapy?

    Scrapy是适用于Python的一个快速、高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据

+   为什么要模拟Scrapy？

    代码复用，大问题化解成小问题



### 模拟Scrapy拆分爬虫框架



```python
import requests
from lxml import etree
from queue import Queue
import threading
import json
from time import sleep

# 爬虫类
class CrawThread(threading.Thread):
    ''' 爬虫类 '''

    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.queue = queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Cookie': 'bid=-ofRRqe5hlw; douban-fav-remind=1; ll="118282"; __yadk_uid=FVVYd6O4JjtGKi0W8VmgU6VO2RW6xdrI; _vwo_uuid_v2=D832BED37911E6A5EBE8543C35B0611A0|aec6cadc2368ac0bd8034120e2eeeb02; __utmc=30149280; __utmc=223695111; push_noty_num=0; push_doumail_num=0; dbcl2="135396251:n7p2/3FAVsU"; ck=tdhO; __utmv=30149280.13539; __utmz=30149280.1610185122.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1610185122.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gads=ID=f80831e1095aabfc-2290817e98c500e1:T=1610185123:RT=1610185123:S=ALNI_MaA715iofhENpz5qAu9GnY4owE2Xg; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1610208283%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCS4OhubC9LpYnaKiVaDQRO2jiwV_ScoCP3BoQiFPZ_arErH6ietpjgtgwHgXBxpi%26wd%3D%26eqid%3Dd90f43a6000f0266000000065ff96bd1%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1119471293.1609947018.1610206460.1610208283.8; __utmb=30149280.0.10.1610208283; __utma=223695111.386314614.1609948853.1610206460.1610208283.7; __utmb=223695111.0.10.1610208283; _pk_id.100001.4cf6=36040234a11eafa0.1609948853.6.1610209232.1610206460.',

        }

    def run(self):
        # 重写run方法
        print(f'启动线程: {self.thread_id}')
        self.schedule()
        print(f'结束线程:{self.thread_id}')

    # 模拟任务调度
    def schedule(self):
        while not self.queue.empty():
            # 队列为空不处理
            page = self.queue.get()
            print(f'下载线程: {self.thread_id}, 下载页面: {page}')
            url = f'https://movie.douban.com/top250?start={page*25}&filter='

            try:
                # downloader下载器
                response = requests.get(url, headers=self.headers)
                dataQueue.put(response.text)
            except Exception as e:
                print('下载出现异常', e)
 



# 页面分析类
class ParserThread(threading.Thread):
    ''' 页面分析类 ''' 
    
    def __init__(self, thread_id, queue, file):
        threading.Thread.__init__(self)     #上面使用了super()
        self.thread_id = thread_id
        self.queue = queue
        self.file = file
    
    def run(self):
        print(f'启动线程: {self.thread_id}')
        while flag:
            try:
                item = self.queue.get(False)    # 参数为false是队列为空，抛出异常
                if not item:
                    continue
                self.parse_data(item)
                self.queue.task_done()  # get之后检测是否会阻塞
            except Exception as e:
                pass

        print(f'结束线程. {self.thread_id}')

    def parse_data(self, item):
       
        ''' 
        解析网页内容的函数 
        : param item: 
        :return:
        '''
        
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="hd"]/a')
            for book in books:
                try:
                    title = book.xpath('./span[1]/text()')
                    link = book.xpath('./@href')
                    response = {
                        'title': title,
                        'link': link
                    }
                    
                    
                    # 解析方法和scrapy相同，再构造一个json
                    json.dump(response, fp=self.file, ensure_ascii=False)
                    self.file.write('\r\n') # 添加换行

                except Exception as e:
                    print('book error', e)
        
        except Exception as e:
            print('page error', e)




if __name__ == '__main__':

    # 定义存放网页的任务队列
    pageQueue = Queue(20)
    for page in range(0, 11):
        pageQueue.put(page)

    # 定义存放解析数据的任务队列
    dataQueue = Queue()

    # 爬虫线程
    crawl_threads = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
    # crawl_name_list = ['crawl_1']
    for thread_id in crawl_name_list:
        thread = CrawThread(thread_id, pageQueue)
        thread.start()
        crawl_threads.append(thread)

    # 将结果保存到一个json文件中
    with open('book.json', 'w+', encoding='utf-8') as pipeline_f:
        
        # 解析线程
        parse_thread = []
        parse_name_list = ['parse_1', 'parse_2', 'parse_3']
        flag = True
        for thread_id in parse_name_list:
            thread = ParserThread(thread_id, dataQueue, pipeline_f)
            thread.start()
            parse_thread.append(thread)

        # 结束crawl线程
        for t in crawl_threads:
            t.join()

        # 结束parse线程
        flag = False
        for t in parse_thread:
            t.join()


    print('退出主线程')


```



