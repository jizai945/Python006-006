
class UserInputError(Exception):
    # 类的初始化
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):
        return self.errorinfo+'123'


userinput = 'a'

try:
    if(not userinput.isdigit()):
        raise UserInputError('用户输入错误')

except UserInputError as ue:
    print(ue)

finally:
    del userinput


