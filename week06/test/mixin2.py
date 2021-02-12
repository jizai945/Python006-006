# 《Python GUI Programing with Tkinter》
# Mixin类无法单独使用， 必须和其他类混合使用，来加强其他类

class Displayer():
    def display(self, message):
        print(message)


class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        # super指的是当前运行的类(MySubClass)的父类
        super(LoggerMixin, self).display(message)
        self.log(message)  # 运行的是MySubClass类下的log


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')


subclass = MySubClass()
subclass.display('This string will be shown and logged in subclasslog.txt')
print(MySubClass.mro())
