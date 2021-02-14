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

##################################
# flash 使用@wraps()的案例
from functools import wraps

# 验证功能
def requires_auth(func):
    @wraps(func)
    def auth_method(*args, **kwargs):
        if not auth:
            authenticate()
        return func(*args, **kwargs)
    return auth_method

@requires_auth
def func_demo():
    pass

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

################################################
# 可以使用wrapt包替代@wraps
## wrapt包 https://wrapt.readthedocs.io/en/latest/quick-start.html
# @wrapt.decorator
# def wrapper(func, instance, args, kwargs):

import wrapt

def with_arguments(myarg1, myarg2):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        return wrapped(*args, **kwargs)
    return wrapper

@with_arguments(1, 2)
def function():
    pass

