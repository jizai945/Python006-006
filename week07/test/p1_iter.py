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
# 类实现完整的迭代器写会议

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
check_iterator(func1())    
