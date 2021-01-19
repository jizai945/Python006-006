from . import Module1   
from .PKG2 import M2

def func2():
    print('import func2')
    Module1.func1()
    M2.m2_func()


