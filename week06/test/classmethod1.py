# 让实例的方法称为类的方法
class K1s1(object):
    bar = 1

    def foo(self):
        print('in foo')

    # 使用类属性、方法

    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()


# 没有实例化，直接使用类的方法
K1s1.class_foo()


#################################
class Story(object):
    snake = 'Python'

    # 初始化函数, 第一个参数必须是self(实例的名字)，
    # 后面的参数代表是这个类可以去接收的参数
    def __init__(self, name):
        self.name = name

    # 类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake


s = Story('anyone')
# get_apple_to_eve 是bound方法，查找顺序是先找s的__dict__是否有get_apple_to_eve,
# 如果没有，查类Story
print(s.get_apple_to_eve)
# 类和实例都可以使用
print(s.get_apple_to_eve())
print(Story.get_apple_to_eve())


##################################
class Kls2():
    def __init__(self, fnmae, lname):
        self.fname = fnmae
        self.lname = lname

    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')


me = Kls2('wilson', 'yin')
me.print_name()


#  输入改为 wilson-yin
# 解决办法1: 修改__init__()
# 解决办法2: 增加__new__() 构造函数
# 解决方法3: 增加 提前处理的函数

# 解决方法3：
def pre_name(obj, name):
    fname, lname = name.split('-')
    return obj(fname, lname)


me2 = pre_name(Kls2, 'wilson-yin')
me2.print_name()


###########################
class Kls3():
    def __init__(self, fnmae, lname):
        self.fname = fnmae
        self.lname = lname

    @classmethod
    def pre_name(cls, name):
        fname, lname = name.split('-')
        return cls(fname, lname)

    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')


me3 = Kls3.pre_name('wilson-yin')
me3.print_name()


###############################
class Fruit(object):
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print(f'calling {cls} , {value}')
        cls.total = value


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass


Apple.set(100)
# calling <class '__main__.Apple'> , 100
Orange.set(200)
# calling <class '__main__.Orange'> , 200
org = Orange()
org.set(300)
# calling <class '__main__.Orange'> , 300

Apple.print_total()
# 100
# 140726992796704
# 140726992799904

Orange.print_total()
# 300
# 140726992796704
# 2368327336944
