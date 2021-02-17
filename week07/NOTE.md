# 学习笔记 python高阶语法



## 变量的赋值

==用来判断两个对象的值是否相等

is用来判断两个是否是同一个对象

python一切皆对象



可变数据类型：

+ 列表 list
+ 字典 dict

不可变数据类型：

+ 整形 int
+ 浮点型 float
+ 字符串型 string
+ 元组 tuple



```python
# 问题1： a、b、c三个id是否相同
a = 123
b = 123
c = a

print(id(a))
print(id(b))
print(id(c))
print(a == b)  # 判断a和b的值是否相等
print(a is b)  # 判断a和b是否是同一个对象

# 问题2： a、b、c的值分别是多少
a = 456
print(id(a))
c = 789
c = b = a  # 连续赋值
print(id(c))


# 问题3：x、y的值分别是什么
x = [1, 2, 3]
y = x
x.append(4)
print(x)
print(y)


# 问题4：a、b的值分别是多少
a = [1, 2, 3]
b = a
a = [4, 5, 6]


# 问题5：a、b的值分别是多少
a = [1, 2, 3]
b = a
a[0], a[1], a[2] = 4, 5, 6

```



## 容器序列的深浅拷贝

序列分类：

+ 容器序列：list、tuple、collections.deque等，能存放**不同类型**的数据。
+ 扁平序列：str、bytes、bytearray、memoryview(内存试图)、array.array等，存放的是**相同类型**的数据 扁平序列只能容纳一种类型

可变类型存在深拷贝、浅拷贝问题

+ 注意：不可变类型(数字、字符串、元组)类型没有拷贝问题

**什么是深拷贝和浅拷贝**：拷贝的时候是否对数据结构里的子结构进行拷贝，比如列表里的子列表



**列表使用 = 赋值，其实这两个对象是相等的，指向同一地址的对象**

**使用list()会在内存里创建一个新的列表去保存**

**使用切片操作，会在内存创建一个新的列表保存**

```python
# 容器序列的拷贝问题

import copy


old_list = [i for i in range(1, 11)]

new_list1 = old_list
new_list2 = list(old_list)
# 这两个不是同一个列表
print(new_list1 is new_list2)  # False


# 切片操作
new_list3 = old_list[:]
print(new_list3 is old_list)  # False


# 嵌套对象
old_list.append([11, 12])
print(old_list)
print(new_list1)
print(new_list2)
print(new_list3)


new_list4 = copy.copy(old_list)  # 浅拷贝
new_list5 = copy.deepcopy(old_list)  # 深拷贝

assert new_list4 == new_list5  # True
assert new_list4 is new_list5  # False

old_list[10][0] = 13
print(old_list)
print(new_list4)  # 浅拷贝，已跟随变化
print(new_list5)

```



## 字典与扩展内置数据类型

字典的key是一个不可变的值， 列表和字典不能作为key

基本数据结构不够用可以使用 collections库去扩展

collections官方文档： https://docs.python.org/zh-cn/3.7/library/collections.html



使用collections扩展内置数据类型

collections提供了加强版的数据类型

+ namedtuple --- 待命名的元组

```python
import collections
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])
x, y = p
print(p.x + p.y)
print(p)
```

+ deque 双向队列
+ Conter 计数器



```python
# 命名元组
from collections import deque
from collections import Counter
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, y=20)
p.x+p.y
p[0] + p[1]
x, y = p


# 计数器
mystring = ['a', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'e']
# 取得频率最高的前三个值
cnt = Counter(mystring)
cnt.most_common(3)
cnt['b']

# 双向队列
d = deque('uvw')
d.append('xyz')
d.appendleft('rst')

```

计算两点的欧式距离， 可以使用numpy

```python
from math import sqrt
from collections import namedtuple
import numpy as np
'''
计算欧式距离
'''

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

op1 = np.sqrt(np.sum(np.square(vector1-vector2)))
op2 = np.linalg.norm(vector1-vector2)


# namedtuple
Point = namedtuple('Point', ['x', 'y', 'z'])


class Vector(Point):
    def __init__(self, p1, p2, p3):
        super(Vector).__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    # 运算符重载
    def __sub__(self, other):
        tmp = (self.p1 - other.p1)**2+(self.p2 -
                                       other.p2)**2+(self.p3 - other.p3)**2
        return sqrt(tmp)


p1 = Vector(1, 2, 3)
p2 = Vector(4, 5, 6)

p1 - p2

```



## 函数的调用

函数 即可调用对象

不带括号传递的是函数的地址，带括号是表示执行函数



## 变量作用域(命名空间)

变量作用域

**其他高级语言**对变量的使用：

+ 变量声明
+ 定义类型(分配内存空间大小)
+ 初始化(赋值、填充内存)
+ 引用(通过对象名称调用对象内存数据)

**Python和高级语言由很大差别**，在模块、类、函数中定义，才有作用域的概念



变量作用域

Python作用域遵循LEGB规则

LEGB含义解释：

+ L-Local(function); 函数内的名字空间
+ E-Enclosing function locals; 外部嵌套函数的名字空间(例如closure)
+ G-Global(module); 函数定义所在模块(文件)的名字空间
+ B-Builtin(Python); Python内置模块的名字空间

```python
# 问题代码1 作用域问题
# def func():
#     var = 100


# func()
# print(var)


# 问题代码2 作用域问题
# def func():
#     print(var)


# func()
# var = 100

#  L G
# 同名不同作用域
x = 'Global'


def func2():
    x = 'Enclosing'

    def func3():
        x = 'Local'

        print(x)
    func3()


print(x)
func2()


# E
x = 'Global'


def func4():
    x = 'Enclosing'

    def func5():
        return x
    return func5


var = func4()
print(var())


# B
print(dir(__builtins__))

```



作用域分析:

```python
# prog1 同名不同作用域问题


x = 1


def func():
    x = 2


func()
print(x)


# prog2 查找顺序问题
y = 2


def func2():
    print(y)


func2()


# prog3 error
def func3():
    z = 3


func3()
print(z)


# prog4 error
def func4():
    print(a)


func4()
a = 100

```



## 函数工具与高阶函数

 函数可以接收不定长参数

**kargs: 关键字参数(key=value的方式)

*args:剩下的非关键字参数

**偏函数**： 指函数必须要带某一些参数

functools.partial: 返回一个可调用的partial对象

使用方法：partial(func, *args, **kw)

偏函数注意：

+ func是必须参数
+ 至少需要一个args或kw参数

高阶函数：函数的参数也是函数

Lambda表达式：Lanbda只是表达式，不是所有的函数逻辑都能封装进去

也叫做匿名的函数

```python
#		x表示传递进来的参数  x+1表示函数执行的内容
k = lambda x:x+1
print(k(1))
```

Lambda表达式后面只能有一个表达式

+ 实现简单函数的时候可以使用Lambda表达式替代
+ 使用高阶函数的时候一般使用Lambda表达式



高阶：参数是函数、返回值是函数

常见的高阶函数：map、reduce、filter、apply

apply在Python2.3被移除，reduce被放在functools包中

推到是和生成器表达式可以替代map和filter函数



**map**工作方式是一种迭代器的方式，每次获取值就是一次迭代

```python
def square(x):
    return x**2


m = map(square, range(10))
next(m)
list(m)
[square(x) for x in range(10)]
dir(m)

```

reduce: 把右侧参数两两进行操作

```python
# reduce
# reduce(f, [x1, x2, x3]) = f(f(x1, x2, x3))
from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 9])
# 25
```

filter：过滤

```python
# filter 过滤
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
```

偏函数：

```python
# 偏函数
def add (x, y):
    return x + y

import functools
add_1 = functools.partial(add, 1)
# 相当于执行 add(1, 10)
add_1(10)

import itertools
g = itertools.count() 
next(g)
next(g)
auto_add_1 = functools.partial(next, g)
auto_add_1() # 自动加一
```

functools 和 itertools是对函数操作经常使用的两个标准库



## 闭包

内部函数对外部函数作用域里变量的引用(非全局变量)则称内部函数为**闭包**

函数返回两个关键字：

+ return

+ yield, 迭代器的方式

返回的对象

+ 可调用对象--闭包(装饰器)

函数里面包含一个函数，外部的函数和内部的函数其实不太相关

```python
# version 4
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))
```



**nonlocal访问外部函数的局部变量**

```python
# 内部函数对外部函数作用域里变量的引用(非全局变量)则称内部函数为闭包

# 实现每次调用加一
def counter(start=0):
    count = [start]
    def incr():
        count[0]+=1
        return count[0]
    return incr

c1 = counter(10)

print(c1())
print(c1())


# nonlocal访问外部函数的局部变量
# 注意start的位置， return的作用域和函数内的作用域不同
def counter2(start=0):
    def incr():
        nonlocal start  # 不用nonlocal无法修改start
        start+=1
        return start
    return incr

c1 = counter2(5)

print(c1())
print(c1())

c2 = counter2(50)

print(c2())
print(c2())

print(c1())
print(c1())

```



## 装饰器介绍

相当于在原有函数上添加了功能，但并不修改原有函数的名字

装饰器：

+ 增强而不改变原有函数

+ 转十圈强调函数的定义态而不是运行态

+ 装饰器语法糖的展开：

  @decorate
  def target(): 等同于 decorate(target)

  ```python
  @decorate
  def target():
      print('do something')    
  # 等同于下面
  
  def target():
      print('do something')
  target = decorate(target)
  ```

  

被装饰函数:

+ 1带参数
+ 2带不定长参数
+ 3带返回值



装饰器在模块导入的时候自动运行

```python
# PEP 318 装饰器 PEP-3129 类装饰器

# 前置问题
def func1():
    pass
a = func1
b=func1()

# func1 表示函数
# func1() 表示执行函数

###############################
# 装饰器， @ 语法糖
@decorate
def func2():
    print('do sth')

# 等效于下面
def func2():
    print('do sth')
func2 = decorate(func2) # 函数其实已经发生了变化，但是函数名没变

#################################


# 装饰器在模块导入的时候自动运行
# testmodule.py
def decorate(func):
    print('running in module')
    def inner():
        return func()
    return inner

# 相当于先执行了 decorate(func2)() 这个函数
@decorate
def func2():
    pass
```

装饰器用在哪里，比如Flask web框架:

```python
# 用在哪里
# Flask的装饰器怎么用的

from flask import Flask

app = Flash(__name__)

@app.route('/')
def index():
    return '<h1>hello world </h1>'

# app.add_url_rute('/', 'index')

if __name__ == '__main__':
    app.run(debug=True)


# 注册
@route('index',methods=['GET','POST'])
def static_html():
    return  render_template('index.html')

# 等效于
static_html = route('index',methods=['GET','POST'])(static_html)()


def route(rule, **options):
    def decorator(f):
        endpoint = options.pop("endpoint", None)
        # 使用类似字典的结构以'index'为key 以 method static_html  其他参数为value存储绑定关系
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator


###############################

# 包装
def html(func):
    def decorator():
        return f'<html>{func()}</html>'
    return decorator

def body(func):
    def decorator():
        return f'<body>{func()}</body>'
    return decorator

@html
@body
def content():
    return 'hello world'

def content2():
    return 'hello world'

content() # 等同于 content没装饰的情况下调用 html(body(content))()
html(body(content2))()

```



## 被装饰函数带参数和返回值的处理

### 被装饰函数带参数

```python
# 被装饰函数带参数
def outer(func):
    def inner(a, b):
        print(f'inner: {func.__name__}') # foo
        print(a, b)
        func(a, b)
    return inner

@outer
def foo(a, b):
    print(a+b)
    print(f'foo: {foo.__name__}') # inner !!! 函数被替换成装饰器的内部函数

foo(1, 2)
foo.__name__
```



### 被装饰函数带不定长参数

```python
def outer2(func):
    def inner2(*args, **kwargs):
        func(*args, **kwargs)
    return inner2

@outer2
def foo2(a, b, c):
    print(a+b+c)

foo2(1, 3, 5)
```



### 被修饰函数带返回值

```python
# 被修饰函数带返回值

def outer3(func):
    def inner3(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return inner3

@outer3
def foo3(a, b, c):
    return (a+b+c)

print(foo3(1, 3, 5))
```

### 装饰器带参数

```python
# 装饰器带参数

def outer_arg(bar):
    def outer(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            print(bar)
            return ret
        return inner
    return outer

# 相当于 outer_arg('foo_arg')(foo)()
@outer_arg('foo_arg')
def foo(a, b, c):
    return (a+b+c)

print(foo(1, 3, 5))

########################################
# 装饰器堆叠

@classmethod
@synchronized(lock)
def foo(cls):
    pass

# 上面等同于下面
def foo(cls):
    pass

foo = synchromized(lock)(foo)
foo = classmethod(foo)
```



## Python内置装饰器

### @wraps(func) 

可以保持原有被装饰的函数的名字(`__name__`)不变

```python
###########################
#内置装饰方法函数

# functools.wraps
# @wraps接受一个函数来进行装饰
# 并加入了赋值函数名称、注释文档、参数列表等等的功能
# 在装饰器里面可以访问在装饰之前的函数的属性
# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 用于在定义包装器函数时发起调用 update_wrapper()作为函数装饰器
# 它等价于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)

from time import ctime, sleep
from functools import wraps
def outer_arg(bar):
    def outer(func):
        # 结构不变增加wraps
        @wraps(func)
        def inner(*args, **kwargs):
            print("%s called at %s"%(func.__name__,ctime()))
            ret = func(*args, **kwargs)
            print(bar)
            return ret
        return inner
    return outer

@outer_arg('foo_arg')
def foo(a, b, c):
    ''' __doc__ '''
    return (a+b+c)

print(foo.__name__)
```

日志记录的时候可以保证，函数名不会被替换掉

```python
####################################

# 日志记录
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func) # 可以保证记录日志的时候函数名不会被替换掉
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__+'was called'
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logint()
def myfunc1():
    pass

myfunc1()
```



在以前的框架中

\# 可以使用wrapt包替代@wraps

\## wrapt包 https://wrapt.readthedocs.io/en/latest/quick-start.html

\# @wrapt.decorator

\# def wrapper(func, instance, args, kwargs):

```python
import wrapt

def with_arguments(myarg1, myarg2):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        return wrapped(*args, **kwargs)
    return wrapper

@with_arguments(1, 2)
def function():
    pass
```



### @lru_cache()

LRU cache的方式可以把最近经常使用的函数的结果保存起来并返回

functolls.lru_cache

《fluent python》的例子

functools.lru_cache(maxsize=128, typed=False)有两个可选参数

maxsize代表缓存的内存占用值，超过这个值之后，旧的结果就会被释放

typed若为True，则会把不同的参数类型得到的结果分开保存

斐波拉契例程：

```python
# functolls.lru_cache
# 《fluent python》的例子
# functools.lru_cache(maxsize=128, typed=False)有两个可选参数
# maxsize代表缓存的内存占用值，超过这个值之后，旧的结果就会被释放
# typed若为True，则会把不同的参数类型得到的结果分开保存

import functools
@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ =='__main__':
    import timeit
    print(timeit.timeit("fibonacci(6)", setup="from __main__ import fibonacci"))
```



## 类装饰器

类装饰器去装饰函数:

```python
# Python 2.6 开始添加类装饰器
from functools import wraps

class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super(MyClass, self).__init__(*args, **kwargs)

    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + 'was called'
            print(func_name)
            return func(*args, **kwargs)
        return wrapped_function

def myfunc():
    pass

MyClass(100)(myfunc)()

# 另一个示例
class Count(object):
    def __init__(self, func):
        self._func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'num of call is {self.num_calls}')
        return self._func(*args, **kwargs)

@Count
def example():
    print('hello')

example()
print(type(example))
```





类装饰器去装饰类

通过类装饰器的方式去装饰修改原有类中的方法:

```python
# 装饰类
def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)
            
        def display(self):
            # 将runtimes()替换为display()
            self.times += 1
            print("run times", self.times)
            self.wrapped.display()
    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number
    # 重写display
    def display(self):
        print("number is",self.number)

six = MyClass(6)
for i in range(5):
    six.display()


```



## 官方文档中的类装饰器代码阅读指南



多看官方文档，了解新特性 PEP

```python
# 官方文档装饰器的其他用途举例

# 同一个函数添加属性
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate

@attrs(versionadded="2.2",
        author="Guido van Rossum")
def mymethod(f):
    pass

################################

# 函数参数观察器
import functools
def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function
@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)

greet('better','me')

####################################

# Python 3.7 引入Data Class PEP557

class MyClass:
    def __init__(self, var_a, var_b):
        self.var_a = var_a
        self.var_b = var_b

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return False
        return (self.var_a, self.var_b) == (other.var_a, other.var_b)
    
var3 = MyClass('x', 'y')
var4 = MyClass('x', 'y')

var3 == var4

from dataclasses import dataclass
@dataclass
class MyClass:
    var_a: str # 类型的提示符
    var_b: str

var_1 = MyClass('x', 'y')
var_2 = MyClass('x', 'y')

# 不在类中重新封装 __eq__

var_1 == var_2
#  存在问题： var_a var_b不能作为类属性访问
```



## 对象协议与鸭子类型

###  实现对象协议用的叫做魔术方法。

对象协议：Duck Typing的概念

容器类型协议：

+ `__str__`打印对象时，默认输出该方法的返回值
+ `__getitem、__setitem__、__delitem__`字典索引操作
+ `__iter__`迭代器
+ `__call__`可调用对象协议  ( 实例化对象.()  时调用 )
+ 比较大小的协议
  + `__eq__` 相等 =
  + `__gt__` 大于 >
  + `__lt__` 小于 <

+ 描述符协议和属性交互协议

  + `__get__` 获取属性时调用

  + `__set__` 设置属性时调用

+ 可哈希对象
  + `__hash__`

上下文管理器：

with 上下文表达式的用法，使用`__enter__() __exit__()`实现上下文管理器



例程：

```python

class Foo(object):
    # 用与方法返回
    def __str__(self):
        return '__str__ is called'

    # 用于字典操作
    def __getitem__(self, key):
        print(f'__getitem__ {key}')

    def __setitem__(self, key, value):
        print(f'__setitem__ {key}, {value}')

    def __delitem__(self, key):
        print(f'__delitem__ {key}')

    # 用于迭代
    def __iter__(self):
        return iter([i for i in range(5)])

# __str__
bar = Foo()
print(bar)

# __XXitem__ 字典
bar['key1']
bar['key1'] = 'value1'
del bar['key1']

# __iter__
for i in bar:
    print(i)
```



### f-string 的字符串输出方式比较好用

`什么时候调用__str__, 什么时候调用__repr__ ?`

正常输出的时候会调用`__str__`

对象之间通信的时候会调用`__repr__`

```python
import math
# %5.3f 5代表输出要保留5个位置 3表示保留小数点后三位
print('The value of Pi is approximately %5.3f.' % math.pi)

#  对1 和 0位置进行输出
print('{1} and {0}'.format('spam', 'eggs'))

print('The story of {0}, {1}, and {other}.'.format(
    'Bill', 'Manfred', other='Georg'))

firstname = 'yin'
lastname = 'wilson'
print('Hello, %s %s.' % (lastname, firstname))
print('Hello, {1} {0}.'.format(firstname, lastname))
print(f'Hello, {lastname} {firstname}.') # f-string


f'{ 2 * 5 }'


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'hello, {self.first_name} {self.last_name}.'

    def __repr__(self):
        return f'hello, {self.first_name} {self.last_name}.'

me = Person('yin', 'wilson')

print(f'{me}')
```



### 类型注解：

提醒参数应该使用的类型， 不会强制类型转换，即使不按照要求传递对应的参数类型也是可以的，但可能执行出问题或出现意想不到的问题    

```python
# typing 类型注解(type hint)

# 与鸭子类型相反的是静态类型，声明变量的时候就要指定类型，如果使用其他类型对变量赋值就会报错

def func(text: str, number: int) -> str:
    return text * number

func('a', 5)
```



## yield语句

return 之后结束了当前函数的生命周期

yield返回之后当前函数暂停



### 生成器-1：

1. 在函数中使用yield关键字，可以实现生成器
2. 生成器可以让函数返回可迭代对象
3. yield和return不同， return返回后, 函数状态终止，yeild保持函数的执行状态，返回后，函数回到之前保存的状态继续执行
4. 函数被yield会暂停，局部变量也会被保存
5. 迭代器终止时，会抛出 Stoplteration异常

### 生成器-2：

方括号替换成小括号括号就变成了一个生成器

```python
print([i for i in range(0,11)])
# 替换为
print((i for i in range (0, 11)))
# 方括号替换成小括号括号就变成了一个生成器

gennumber = (i for i in range(0,11))
print(next(gennumber))
print(next(gennumber))
print(next(gennumber))
# print(list(gennumber))
print([i for i in genumber])

```

### 生成器-3：

lterables: 可迭代 `包含 __getitem__()或__iter__()方法的容器对象`

lterator: 迭代器 `包含next()和__iter__()方法`

Generator: 生成器 包含yield语句的函数



next()的魔术方法是`__next__`

列表是可迭代的：

```python
alist = [1, 2, 3, 4, 5]
hasattr( alist, '__iter__' ) # True
hasattr( alist, '__next__' ) # False

for i in alist:
    print(i)

# 结论一 列表是可迭代对象，或称为可迭代(iterable),
#           不是迭代器(iterator)

# __iter__方法是 iter()函数所对应的魔术方法，
# __next__方法是 next()函数所对应的魔术方法
######################################################
```

迭代器函数只有执行的时候 如`func()` 才是迭代器，而 func不是

```python
alist = [1, 2, 3, 4, 5]
hasattr( alist, '__iter__' ) # True
hasattr( alist, '__next__' ) # False

for i in alist:
    print(i)

# 结论一 列表是可迭代对象，或称为可迭代(iterable),
#           不是迭代器(iterator)

# __iter__方法是 iter()函数所对应的魔术方法，
# __next__方法是 next()函数所对应的魔术方法
######################################################

g = (i for i in range(5))
g # <generator object>

hasattr(g, '__iter__') # True
hasattr(g, '__next__') # True

g.__next__()
next(g)
for i in g:
    print(i)

# 结论二 生成器实现完整的迭代器协议

####################################################
# 类实现完整的迭代器协议

class SampleIterator:
    def __iter__(self):
        return self
    
    def __next__(self):
        #  Not The End
        if ...:
            return ...
        # Reach The End
        else:
            rasie StopIteration
        
# 函数实现完整的迭代器协议
def SampleGenerator():
    yield ...
    yield ...
    yield ... # yield语句
# 只要一个函数的定义中实现了yield关键词，则此函数将不再是一个函数，
# 而成为一个 "生成器构造函数"，调用此构造函数即可产生一个生成器对象

###########################################
# check iter
def check_iterator(obj):
    if hasattr(obj,'__iter__'):
        if hasattr(obj, '__next__'):           
            print(f'{obj} is a iterator') # 完整迭代器协议
        else:
            print(f'{obj} is a iterable') # 可迭代对象
    else:
        print(f'{obj} can not iterable') # 不可迭代

def func1():
    yield range(5)

check_iterator(func1) # 对象操作是不可迭代
check_iterator(func1())  # 是一个迭代器  

```



 ## 迭代器使用的注意事项

迭代器的作用是实现了迭代器协议

 itertools的三个常见无限迭代器:

```python
# itertools的三个常见无限迭代器
import itertools

count = itertools.count() # 计数器
next(count)
next(count)
next(count)

#######################################
cycle = itertools.cycle( ('yes', 'no') ) # 循环遍历
next(cycle)
next(cycle)
next(cycle)
next(cycle)

#########################################
repeat = itertools.repeat(10, times=2) # 重复 times是限制次数
# repeat = itertools.repeat(10)
next(repeat)
next(repeat)
next(repeat)

########################################
# 有限迭代器
for j in itertools.chain('ABC', [1, 2, 3]):
    print(j)

# Python3.3 引入了 yield from
# PEP-380
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

s = 'ABC'
t = [1, 2, 3]

test = chain(s, t)
next(test)

list(chain(s, t))

# 上面等同于下面
def chain2(*iterables):
    for i in iterables:
        yield from i # 替代内层循环

s = 'ABC'
t = [1, 2, 3]

test = chain2(s, t)
next(test)

list(chain2(s, t))       
```



\# RuntimeError: 字典进行插入操作后，字典迭代器会立即失效

\# 列表不会出问题，尾插入操作不会损坏指向当前元素的List迭代器，列表会自动变长，但是出现StopIteration的时候再插入，不会再迭代

\# 迭代器一旦耗尽，永久损坏

```python
# 迭代器有效性测试
a_dict = {'a':1, 'b':2}
a_dict_iter = iter(a_dict)

next(a_dict_iter)

a_dict['c'] = 3
next(a_dict_iter)
# RuntimeError: 字典进行插入操作后，字典迭代器会立即失效
a_list = [1, 2, 3, 4, 5]
a_list_iter = iter(a_list)

next(a_list_iter)

a_list.append(6)
next(a_list_iter)
# 尾插入操作不会损坏指向当前元素的List迭代器，列表会自动变长

# 迭代器一旦耗尽，永久损坏
x = iter([ y for y in range(5)])
for i in x:
    i
x.__next__()

```



## yield表达式

yield可以传入参数 通过iterator.send

```python
def jumping_range(up_to):
    index = 0
    while index < up_to:
        jump = yield index
        print(f'jump is {jump}')
        if jump is None:
            jump = 1 # next() 或者 send(None)
        index += jump
        print(f'index is {index}')

if __name__ == '__main__':
    iterator = jumping_range(5)
    print(next(iterator)) # 0 调用next()相当于send(None)
    print(iterator.send(2)) # 2
    print(next(iterator)) # 3
    print(iterator.send(-1)) # 2
    for x in iterator: # 相当于调用next()
        print(x) # 3
```

通过yield可以实现协程的工作模式



## 协程简介

多线程用来提高我们的并发程序的运行效率

协程是用来提高IO密集型的程序的工作效率

协程和线程的区别：

+ 协程是异步的，线程是同步的
+ 协程是非抢占式，线程是抢占式的
+ 线程是被动调度的，协程是主动调度的
+ 协程可以暂停函数的执行，保留上一次调用时的状态，是增强型生成器
+ 协程是用户级的任务调度，线程是内核级的任务调度
+ 协程适用于IO密集型程序，不适用于CPU密集型程序的处理



### 异步编程

python3.5 版本引入了 await取代了yield from方式、

函数必须使用async这个关键字 async 和 await成对出现

是一种事件循环机制

```python
import asyncio
async def py35_coro():
    await stuff()
```

注意：await接收的对象必须是awaitable对象

awaitable对象定义了`__await__()`方法

awaitable对象有三类：

1. 协程coroutine
2. 任务Task
3. 未来对象Future



```python
# python 3.4 支持事件循环的方法
import asyncio

@asyncio.coroutine
def py34_func():
    yield from sth()


########################################
# python3.5 增加async await
async def py35_func():
    await sth()

```



asyncio 中的sleep

```python
import asyncio
async def main():
    print('hello')
    await asyncio.sleep(3)
    print('world')

# asyncio.run()运行最高层级的conroutine
asyncio.run(main())
# hello
# sleep 3 second
# world

```



### 协程调用过程： 

\# 调用协程时，会被注册到ioloop，返回coroutine对象

\# 用ensure_future 封装为Future对象

\# 提交给ioloop



\# 官方文档

\# https://docs.python.org/zh-cn/3/library/asyncio-task.html



## aiohttp简介

可以用来搭建一个服务器:

```python
# Web Server
from aiohttp import web

# views
async def index(request):
    return web.Response(text='hello aiohttp')

# routes
def setup_routes(app):
    app.router.add_get('/', index)

# app
app = web.Application()
setup_routes(app)
web.run_app(app, host='127.0.0.1', port=8080)


# 官方文档
# https://hubertroy.gitbooks.io/aiohttp-chinese-documentation/content/aiohttp%E6%96%87%E6%A1%A3/ServerTutorial.html
```



### asyncio 协程任务

异步HTTP请求:

```python
import aiohttp
import asyncio

url = 'http://httpbin.org/get'

async def fetch(client, url):
    # get 方式请求url
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.text()

async def main():
    # 获取session对象
    async with aiohttp.ClientSession() as client:
        html = await fetch(client, url)
        print(html)

loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
# Zero-sleep 让底层连接得到关闭的缓冲时间
loop.run_until_complete(asyncio.sleep(0))
loop.close()
```



### 使用协程请求多个HTTP请求：

```python
import aiohttp
import asyncio

urls = [
    'http://httpbin.org',
    'http://httpbin.org/get',
    'http://httpbin.org/ip',
    'http://httpbin.org/headers'
]

async def  crawler():
    async with aiohttp.ClientSession() as session:
        futures = map(asyncio.ensure_future, map(session.get, urls))
        for task in asyncio.as_completed(futures):
            print(await task)

if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asyncio.ensure_future(crawler()))
```



### 协程配合多进程

实际工作中可以把下面test函数改成真正要执行的函数

```python
# 进程池和协程

from multiprocessing import Pool
import asyncio
import time


async def test(time):
    await asyncio.sleep(time)

async def main(num):
    start_time = time.time()
    tasks = [asyncio.create_task(test(1)) for proxy in range(num)]
    [await t for t in tasks]
    print(time.time() - start_time)


def run(num):
    asyncio.run(main(num))


if __name__ == "__main__":
    start_time = time.time()
    p = Pool()
    for i in range(4):
        p.apply_async(run, args=(2500,))
    p.close()
    p.join()
    print(f'total {time.time() - start_time}')
```

