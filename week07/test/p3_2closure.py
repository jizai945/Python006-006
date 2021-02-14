# version 2
# 如果line()的定义中引用了外部的变量
def line_Conf():

    b = 10
    def line(x):
        return 2*x+b
    return line

my_line = line_Conf()
print(my_line(5))