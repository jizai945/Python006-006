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

