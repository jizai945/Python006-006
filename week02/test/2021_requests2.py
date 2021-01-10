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




