# GOD
class Human(object):
    def __init__(self, name):
        self.name = name


h1 = Human('Adam')
h2 = Human('Eve')

# 对实例属性做修改
h1.name = 'python'

# 对实例属性查询
h1.name

# 删除实例属性
del h1.name

# AttributeError 访问不存在的属性
# 由__getattribute__(self, name)抛出
# h1.name

#############


class Human2(object):
    '''
    getattribute对任意读取的属性进行拦截
    '''

    def __init__(self):
        self.age = 18

    def __getattribute__(self, item):
        print(f'__getattribute__called item:{item}')
        try:
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item] = 100
            return 100


h1 = Human2()

h1.age
print(h1.noattr)
