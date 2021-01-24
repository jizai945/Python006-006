###
# 要求使用 MySQL 存储短评内容（至少 20 条）以及短评所对应的星级；
# ###

# 爬虫

import requests
from lxml import etree
from queue import Queue
import threading
import json
from time import sleep

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import re

Base = declarative_base()

class comment_table(Base):
    __tablename__ = 'IronManOrm'
    comment_id = Column(Integer(), primary_key=True)
    starts = Column(Integer())
    content = Column(String(512), index=True)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
cookie = 'll="118282"; bid=t3UXZa8JcCQ; push_noty_num=0; push_doumail_num=0; douban-fav-remind=1; dbcl2="135396251:ANG/wbor0Tg"; ck=6zVC'

# 爬虫类
class CrawThread(threading.Thread):
    ''' 爬虫类 '''

    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.queue = queue
        self.headers = {
            'User-Agent': user_agent,
            'Cookie': cookie,

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
            url = f'https://movie.douban.com/subject/1432146/comments?start={page*20}&limit=20&status=P&sort=new_score'

            try:
                # downloader下载器
                response = requests.get(url, headers=self.headers)
                dataQueue.put(response.text)
                sleep(0.1)
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
            items = html.xpath('//div[@class="comment"] ')

            my_dict = {'力荐':5, '推荐':4, '还行':3, '较差':2, '很差':1}

            for it in items:
                try:
                    #  星级
                    starts = it.xpath('./h3/span[2]/span[2]/@title')
                    starts_num = my_dict[''.join(starts)]
                    # 评论
                    commemt = it.xpath('./p/span/text()')
                    
                    response = {
                        'starts': starts_num,
                        'commemt': commemt
                    }
                    # print(response)
                     
                    # 解析方法和scrapy相同，再构造一个json
                    json.dump(response, fp=self.file, ensure_ascii=False)
                    self.file.write('\r\n') # 添加换行

                    demo = comment_table(starts=starts_num, content=''.join(commemt))
                    session.add(demo)    

                except Exception as e:
                    print('response error', e)
        
        except Exception as e:
            print('page error', e)


if __name__ == '__main__':

    # 实例化一个引擎
    dburl='mysql+pymysql://testuser:testpass@192.168.0.106:3306/week04db?charset=utf8mb4'
    engine=create_engine(dburl, echo=True, encoding='utf-8', )

    Base.metadata.create_all(engine)

    # 创建session 理解为产生一个映射的类
    SessionClass = sessionmaker(bind=engine)
    # 实例化
    session = SessionClass()
    query = session.query(comment_table)

    page_s = 10

    # 定义存放网页的任务队列
    pageQueue = Queue(page_s)
    for page in range(0, page_s):
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
        sleep(0.2)
        crawl_threads.append(thread)

    # 将结果保存到一个json文件中
    with open('commet.json', 'w+', encoding='utf-8') as pipeline_f:
        
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

    session.flush()
    session.commit()


    print('退出主线程')



