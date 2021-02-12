# 装饰器实现单实例模式
import World


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class MyClass:
    pass


m1 = MyClass()
m2 = MyClass()
# 两个id是一样
print(id(m1))
print(id(m2))


############################
# __new__ 与 __init__的关系
class Foo(object):
    def __new__(cls, name):
        print('trace __new__')
        return super().__new__(cls)

    def __init__(self, name):
        print('trace __init__')
        super().__init__()
        self.name = name


bar = Foo('test')
bar.name


###############################
# __new__方式实现单实例模式
class Singleton2(object):
    __isintance = False  # 默认没有被实例化

    def __new__(cls, *args, **kwargs):
        if cls.__isintance:
            return cls.__isintance  # 返回实例化对象
        cls.__isintance = object.__new__(cls)  # 实例化
        return cls.__isintance
# 以上会存在线程安全的问题


# 方法1，实现__new__方法
# 并在将一个类的实例绑定到类变量__instance上，
# 如果cls.__instance为None说明该类还没有实例化过，实例化该类，并返回
# 如果cls.__instance部位None，直接返回cls.__instance
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(
                cls, *args, **kargs
            )

        return cls.__instance


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)

# 解决并发， 引入带锁版


class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls, &= *args, **kargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()  # 加锁
        try:
            if cls in cls.objs:  # double check locking
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()  # 释放锁

# 利用经典的双检查锁机制，确保了在并发环境下Singleton的正确实现
# 但这个方案并不完美， 至少还有以下两个问题：
# 如果Singleton的子类重载了__new__()方法， 会覆盖或者干扰Singleton类中的__new__()的执行
# 虽然这种清空出现的概率极小，但不可忽视
# 如果子类由__init__()方法, 那么每次实例化该Singleton的时候
# __init__()都会被调用到，这显然是不应该的， __init__()至英国在创建实例的时候被调用一次
# 这两个问题当然可以解决，比如通过文档告知其他程序员，子类化Singleton的时候，请务必记得调用父类的__new__()方法；
# 而第二个问题也可以通过偷偷地替换掉__init__()方法来确保它只调用一次。
# 但是，为了实现一个单例，做大量的、水面之下的工作让人感觉相当不Pythonic。
# 这也引起了Python社区的反思，有人开始重新审视Python的语法元素，发现模块采用的其实是天然的单例的实现方式。
# ·所有的变量都会绑定到模块。
# ·模块只初始化一次。
# ·import机制是线程安全的（保证了在并发状态下模块也只有一个实例）。
# 当我们想要实现一个游戏世界时，只需简单地创建World.py就可以了。


# World.py
# import Sun
def run():
    while True:
        Sun.rise()
        Sun.set()


# main.py
# import World
World.run()
