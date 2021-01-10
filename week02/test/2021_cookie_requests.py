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
