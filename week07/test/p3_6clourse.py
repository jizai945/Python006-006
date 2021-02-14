# 内部函数对外部函数作用域里变量的引用(非全局变量)则称内部函数为闭包

# 实现每次调用加一
def counter(start=0):
    count = [start]
    def incr():
        count[0]+=1
        return count[0]
    return incr

c1 = counter(10)

print(c1())
print(c1())


# nonlocal访问外部函数的局部变量
# 注意start的位置， return的作用域和函数内的作用域不同
def counter2(start=0):
    def incr():
        nonlocal start  # 不用nonlocal无法修改start
        start+=1
        return start
    return incr

c1 = counter2(5)

print(c1())
print(c1())

c2 = counter2(50)

print(c2())
print(c2())

print(c1())
print(c1())
