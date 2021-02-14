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
