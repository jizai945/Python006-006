# 父类
class People(object):
    def __init__(self, name):
        self.gene = 'XY'
        # 假设人人都有名字
        self.name = name

    def walk(self):
        print('I can walk')


# 子类
class Man(People):
    def __init__(self, name):
        # 找到Man的父类People， 把类People的对象转换Man的对象
        super().__init__(name)

    def work(self):
        print('work hard')


def Woman(People):
    def __init__(self, name):
        super().__init__(name)

    def shopping(self):
        print('buy buy buy')


p1 = Man('Adam')
p2 = Woman('Eve')

# 问题1 gene有没有被继承？
# super().__init__(name)
p1.gene

# 问题2 People的父类是谁？
# object 与 type
print('object', object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)
# type元类是由type自身创建， object类由元类type创建
# type类继承了objcect

# 问题3 能否实现多重层级继承
# 可以


# 问题4 能否实现多个父类同时继承
# 可以
class Son(Man, Woman):
    pass
