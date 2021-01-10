# 学习笔记



## 版本差异

官方文档 ： https://www.python.org/doc/versions/

查看版本差异: https://docs.python.org/zh-cn/3/

python3和python2 不完全兼容



工作中都在用哪个版本：

Python3.7的版本



安装：https://www.python.org/downloads/



## python交互模式的使用

python和pip命令：

1.  python命令： python的解释器,官方采用CPython版本
2.  pip命令：方便安装第三方库



REPL（交互式解释器）：

1.  python程序可以交互执行也可以采用文件加载执行
2.  IPython可以扩展python的交互功能





## pip安装加速

国内常见的镜像站：

1.   豆瓣: http://pypi.doubanio.com/simple/
2.   清华: **https://pypi.tuna.tsinghua.edu.cn/simple**

升级pip:

1.  方法一：

    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

2.  方法二：

    pip config set global.index-url http://pypi.doubanio.com/simple/

    pip install pip -U

​	配置文件：

windows: c:\User\xxx\pip\pip.ini

Linux: ~/.pip/pip.conf



## python IDE

1.  pycharm

2.   ==vscode==

    vscode左下角可以选择python版本

    好用插件:rainbow fart 多个括号的时候方便看 

    alt+↑ 或者 alt+↓可以交换两行代码

3.  Jupyter Notebook



## 一般开发流程

```
1. 搞清需求
2. 编写源代码
3. 使用Python解释器转换为目标代码
4. 运行程序
5. 测试
6. 修复错误
7. 再运行、测试
8. 。。。
```



## 迁移部署(虚拟环境)

	1. 在生存环境中虚拟环境是保持环境一致性的必备工具
	2. 开发环境中可以不配置虚拟环境



一些命令

```shell
# 在文件夹中建立一个新的虚拟环境
python -m venv (虚拟环境目录 venv)
# 使用当前的虚拟环境 windows
source Scripts/activate
# 使用当前的虚拟环境 linux
source bin/activate
# 使用pip安装外部包也是会放到虚拟环境里
pip install ipython
# 取消当前虚拟环境
deactivate
# 查看python的版本环境
which python
# 查看pip的版本环境
which pip
# 查看当前环境下安装的软件包和版本
pip freeze


# 使用pip安装外部包也是会放到虚拟环境里

```



### 开发环境迁移到生产环境

```shell
# 1.把.py文件拷贝到生成环境的文件夹中
cp venv1/src/a.py venv1/src/
# 2. 查看当前开发环境中的版本,并且在生产环境中安装相同版本的python
python -V
# 使能开发环境
source venv1/Scripts/activate
# 查看开发环境中使用到了哪些第三方包
pip freeze
# 把当前安装的包保存到一个文件里面
pip freeze > requirements.txt
# 离开开发环境
deactivate
# 激活生产环境
source venv2/Scripts/activate
# ***查看当前生产环境和开发环境版本对不对应
python -V
pip -V
# 从文件中选择安装包
pip install -r requirements.txt


# 最后生产环境安装的包和开发环境相同了
```





## python基础数据类型



|                    |                    |
| :----------------: | :----------------: |
|        None        |       空对象       |
|        Bool        |       布尔值       |
|        数值        | 整数、浮点数、复数 |
|     序列 -- []     | 字符串、列表、元组 |
|     集合 -- {}     |        字典        |
| 元组(不可变) -- () |                    |
|       可调用       |        函数        |



## python高级数据类型

|             |              |
| ----------- | ------------ |
| collections | 容器数据类型 |
| nametuple() | 命名元组     |
| deque       | 双端队列     |
| Counter     | 计数器       |
| OrderedDict | 有顺序的字典 |



文档地址： https://docs.python.org/zh-cn/3.7/library/collections.html



## 控制流

缩进很重要

pythonic  ： python风格化的代码

```python
# 循环遍历
list = ['a', 'b', 'c']
for i in list:
	print(i)
    
if True:
    print('True')
else:
    print('??')
    

```



## 函数和模块的区别



```
函数、模块和包的区别是什么？


一个.py的文件就可以是一个模块


```



```python
# 导入模块的时候下面这块就不会执行
# 一般把函数的定义放在 if __name__ == '__main__'之前，函数的运行或者调试的代码放在后面
if __name__ == '__main__'
	print('123')
```



## 标准库：



常见模块
1. time		时间
2. datetime   日期
3. logging  日志定位问题
4. random  随机数
5. json  特定格式json
6. pathlib  文件路径处理
7. os.path  文件路径处理



### 日期时间处理 datetime 和 timedelta



```python
# 打印时间戳
time.time()
# 本地时间
time.localtime()
# 打印时间较为直观
time.strftime('%Y-%m-%d %X', time.localtime())
# 把时间转换出来
time.strptime('2020-12-30 00:21:26','%Y-%m-%d %X')

# 使用下面的方式引用较为方便
import datetime
datetime.datetime.today() #较麻烦

from datetime import datetime
from datetime import * # 或者这种方式
datetime.today()
```



### 日志处理 logging

```
好处：
1. 格式规整
2. 不需要人为设置各种复杂的规则
3. 线程安全
4. 可以设置日志等级
...

```

#### 配置

logging.basicConfig()



| 格式       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| *filename* | 使用指定的文件名而不是 StreamHandler 创建 FileHandler。      |
| *filemode* | 如果指定了 *filename*，则用此 [模式](https://docs.python.org/zh-cn/3.7/library/functions.html#filemodes) 打开该文件。 默认模式为 `'a'`。 |
| *format*   | 处理器使用的指定格式字符串。                                 |
| *datefmt*  | 使用指定的日期/时间格式，与 [`time.strftime()`](https://docs.python.org/zh-cn/3.7/library/time.html#time.strftime) 所接受的格式相同。 |
| *style*    | 如果指定了 *format*，将为格式字符串使用此风格。 `'%'`, `'{'` 或 `'$'` 分别对应于 [printf 风格](https://docs.python.org/zh-cn/3.7/library/stdtypes.html#old-string-formatting), [`str.format()`](https://docs.python.org/zh-cn/3.7/library/stdtypes.html#str.format) 或 [`string.Template`](https://docs.python.org/zh-cn/3.7/library/string.html#string.Template)。 默认为 `'%'`。 |
| *level*    | 设置根记录器级别去指定 [level](https://docs.python.org/zh-cn/3.7/library/logging.html#levels). |
| *stream*   | 使用指定的流初始化 StreamHandler。 请注意此参数与 *filename* 是不兼容的 - 如果两者同时存在，则会引发 `ValueError`。 |
| *handlers* | 如果指定，这应为一个包含要加入根日志记录器的已创建处理程序的可迭代对象。 任何尚未设置格式描述符的处理程序将被设置为在此函数中创建的默认格式描述符。 请注意此参数与 *filename* 或 *stream* 不兼容 —— 如果两者同时存在，则会引发 `ValueError`。 |



#### 日志写入

1.   先进入一个要写入日志的文件路径

```python
import logging

logging.basicConfig(filename='test.log')
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

# 默认追加方式
logging.basicConfig(filename='test.log', 
                    level=logging.DEBUG,
                   	datefmt='%Y-%m-%d %H:%M:%S',
                   	format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')
```



## 路径处理



```python
from pathlib import Path
p = Path()
p.resolve() # 当前的完整路径

path = 'F:\keil\mdk526.exe'
p = Path(path)
p.name
p.stem
p.suffix
p.suffixes  # 获取双扩展名
p.parent
p.parents
for i in p.parents:
    print(i)
p.parts


import os
os.path.abspath('test.log') # 获取完整路径
os.path.basename(path) # 获取当前路径字符串中的文件名
os.path.dirname(path) # 获取当前路径字符串中的路径
os.path.exists('/ect/passwd') # 判断文件是否存在
os.path.isfile('/ect/passwd') # 判断是否是文件
os.path.isdir('/ect/passwd') # 判断是否是路径
os.path.join('a', 'b') # 路径的连接
os.path.join('/a', 'b') # 路径的连接


```



## 守护进程(daemon)

Windows里面叫服务

Linux里面叫daemon进程

可以脱离终端，终端关闭了，程序也还能进行





## 正则表达式 -- re模块

作用，对字符串：

1.匹配

2.提取子串

3.替换



官方文档： https://docs.python.org/zh-cn/3.7/library/re.html



```python
prog = re.compile(pattern)
result = prog.match(string)
# 等价于
result = re.match(pattern, string)
#如果需要多次使用这个正则表达式的话，使用 re.compile() 和保存这个正则对象以便复用，可以让程序更加高效。
```



```python
import re

content = '12332112312'
# 判断是否是11位号码
re.match(".{11}"， content)
# 把匹配的获取出来
re.match(".{11}", content).group()
# 把匹配成功的位置获取出来
re.match(".{11}", content).span()

re.match('.*@.*', '123@123.com')
re.match('.*@.*', '123@123.com').group()
# 可以使用()分组，然后group可以取得分组的信息
re.match('(.*)@(.*)', '123@qq.com').group(1)

# 查找
re.search('@', '123@qq.com')
# 找到所有匹配的
re.findall('@', '123@123.com')

# 替换 参数1：要替换的字符串 参数2：替换后的内容字符串  参数3：匹配的字符串
re.sub('123', '456', '123@123.com')
# \d匹配单个数字
re.sub('\d+', 'xyz', '123@123.com')

#字符串分割，返回的是一个列表
re.split('@', '123@123.com')
# ()保留分割的符号
re.split('(@)', '123@123.com')
```





