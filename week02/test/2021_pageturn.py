# 翻页的处理
import requests
from lxml import etree
from time import sleep
# 控制请求的频率 引入了time模块

# 使用了def定义函数 myurl是函数的参数
def get_url_name(myurl):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    headers = {
        'User-Agent': ua,
         'Cookie': 'bid=-ofRRqe5hlw; douban-fav-remind=1; ll="118282"; __yadk_uid=FVVYd6O4JjtGKi0W8VmgU6VO2RW6xdrI; _vwo_uuid_v2=D832BED37911E6A5EBE8543C35B0611A0|aec6cadc2368ac0bd8034120e2eeeb02; __utmc=30149280; __utmc=223695111; push_noty_num=0; push_doumail_num=0; dbcl2="135396251:n7p2/3FAVsU"; ck=tdhO; __utmv=30149280.13539; __utmz=30149280.1610185122.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1610185122.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gads=ID=f80831e1095aabfc-2290817e98c500e1:T=1610185123:RT=1610185123:S=ALNI_MaA715iofhENpz5qAu9GnY4owE2Xg; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1610208283%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCS4OhubC9LpYnaKiVaDQRO2jiwV_ScoCP3BoQiFPZ_arErH6ietpjgtgwHgXBxpi%26wd%3D%26eqid%3Dd90f43a6000f0266000000065ff96bd1%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1119471293.1609947018.1610206460.1610208283.8; __utmb=30149280.0.10.1610208283; __utma=223695111.386314614.1609948853.1610206460.1610208283.7; __utmb=223695111.0.10.1610208283; _pk_id.100001.4cf6=36040234a11eafa0.1609948853.6.1610209232.1610206460.',
        }
    response = requests.get(myurl, headers=headers)
    print(response.text)
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