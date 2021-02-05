from functools import wraps

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print(args)
            print('666')
            print ("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print ("say {}!".format(something))

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something, num, key=None):
    print ("do {}...".format(something))

if __name__ == '__main__':
    say('hello')
    do("my work", 23)