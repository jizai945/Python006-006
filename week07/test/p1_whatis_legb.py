# 问题代码1 作用域问题
# def func():
#     var = 100


# func()
# print(var)


# 问题代码2 作用域问题
# def func():
#     print(var)


# func()
# var = 100

#  L G
# 同名不同作用域
x = 'Global'


def func2():
    x = 'Enclosing'

    def func3():
        x = 'Local'

        print(x)
    func3()


print(x)
func2()


# E
x = 'Global'


def func4():
    x = 'Enclosing'

    def func5():
        return x
    return func5


var = func4()
print(var())


# B
print(dir(__builtins__))
