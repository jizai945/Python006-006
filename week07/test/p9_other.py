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

