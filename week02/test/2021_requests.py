# 使用requests库获取豆瓣影评

import requests

# 浏览器版本
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

print(response.text)
print(f'返回码是:{response.status_code}')


