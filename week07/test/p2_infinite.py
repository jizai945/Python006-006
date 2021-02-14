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