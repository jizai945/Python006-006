import time

def timer(func):
    def inner2(*args, **kwargs):
        start = time.clock()
        ret = func(*args, **kwargs)
        elapsed = (time.clock() - start)
        print(f"Time used:{elapsed}")
        
        return ret
    return inner2


@timer
def test(*args, **kwargs):
    print(f'hello, args:{args}, kwargs:{kwargs}')


def fib(x: int)->int:
    if x == 0:
        return 0
    if x <= 2:
        return 1
    else :
        return fib(x-1) + fib (x-2)

@timer
def fib_run(x: int)->int:
    return fib(x)

if __name__ == '__main__':

    test(1, 2, 3, a=5)

    print(f'fib = {fib_run(20)}')

    

