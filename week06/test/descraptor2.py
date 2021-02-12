# GOD
class Human(object):
    def __init__(self, name):
        self.name = name

    # 将方法封装成属性
    @property
    def gender(self):
        return 'M'


h1 = Human('Adam')
h2 = Human('Eve')
h1.gender

# AttributeError:
h2.gender = 'F'


###########################

class Human(object):
    def __init__(self):
        self._gender = None

    # 将方法封装成属性
    @property
    def gender2(self):
        return 'M'

    # 支持修改
    @gender2.setter
    def gender2(self, value):
        self._gender = value

    # 支持删除
    @gender2.deleter
    def gender2(self):
        del self._gender


h = Human()
h.gender = 'F'
h.gender
del h.gender
# 另一种property写法
# gender = property(get__, set__, del__, 'other propetry')

# 被修饰函数建议使用相同的gender2（函数名）
# 使用setter 并不能真正意义上实现无法写入, gender被改名为 _Article_gender


# property本质并不是函数， 二十特殊类(实现了数据描述符的类)
# 如果一个对象同时定义了__get__()和__set__()方法, 则成为数据描述符
# 如果仅定义了__get__()的方法，则成为非数据描述符

# property的优点:
# 1 代码更简洁、可读性、可维护性更强
# 2 更好的管理属性的访问
# 3 控制属性访问权限、提高数据安全性

#############################
# property 纯python实现

class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
            self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
