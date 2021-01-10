# 使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 
# 话题：如何看待推特永久停用特朗普个人账号？

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
            'Cookie': '_zap=0f805485-ed2a-40d3-982c-462bf42444f3; d_c0="AABT20ElShKPTqdn5dJfvP0l08KzNSolgwc=|1606993468"; _xsrf=0ede3f50-9bf5-413d-a1b2-fcb5a63252d0; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1609180860,1609180921,1610209002,1610219373; capsion_ticket="2|1:0|10:1610219374|14:capsion_ticket|44:NmI5NjE0MWVhZTJjNGE0OTllZjFlOGE0MTY3MWJlZDY=|c8f5c02094e9862370656dcf0b6a91a2a904d9eaa03268bf6ed49a0d85d14f56"; SESSIONID=1hJYWyb1q1rGOG2aVO3WD3gVs5KDrGU3KCaE5CNilhw; JOID=UV8XC01DHAdpRxjMFEjtUIGJ7_IHdnFHPhVlqy83KXAkBlr6cC3s-j1GGcMQ5FG3wq0UmAPj3lGX2tjl9j-ref4=; osd=UFwVA01CHwVhRxnPFkDtUYKL5_IGdXNPPhRmqSc3KHMmDlr7cy_k-jxFG8sQ5VK1yq0VmwHr3lCU2NDl9zypcf4=; z_c0="2|1:0|10:1610219395|4:z_c0|92:Mi4xcVNJcUF3QUFBQUFBQUZQYlFTVktFaVlBQUFCZ0FsVk5nMDNuWUFENXBqb3kwaGZranloYlAzTkczVFYtbmtfRDBn|148e223cd15a2901ba7033ac057c3122140d7ccc785be572e1545d5bf001c54a"; unlock_ticket="ADDAidOlHAomAAAAYAJVTYsG-l-DSoMB0J0jqRaxDn9Kfk4PfLZ7xA=="; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1610219652; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1610219668|1610219373',

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
            url = f'https://www.zhihu.com/question/438537142'

            try:
                # downloader下载器
                response = requests.get(url, headers=self.headers)
                print(response.status_code)
                dataQueue.put(response.text)
                with open('./index.html', 'w+', encoding='utf8') as f:
                    f.write(response.text)
                    
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
            user = html.xpath('//div[@class="RichContent-inner"]/span')
            i = 0
            for u in user: 
                i += 1
                books = u.xpath('./p')
                for book in books:
                    try:
                        text = book.xpath('./text()')
                        # print(text)
                        response = {
                            '用户'+str(i): text,
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
    for page in range(0, 1):
        pageQueue.put(page)

    # 定义存放解析数据的任务队列
    dataQueue = Queue()

    # 爬虫线程
    crawl_threads = []
    # crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
    crawl_name_list = ['crawl_1']
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

