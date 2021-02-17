def square(x):
    return x**2

def mymap(func, *iterables):
    for args in zip(*iterables):
        yield(func(*args))

if __name__ == '__main__':

    a = mymap(square, range(10))
    print(next(a))
    print(next(a))
    print(list(a))