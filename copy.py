import logging

'''
def use_logging(func):
    logging.warn('%s is running'%func.__name__)
    func()

def bar():
    print('i am bar')

def use_logging(func):
    def wrapper(*args,**kwargs):
        logging.warn('%s is running'%func.__name__)
        return func(*args,**kwargs)
    return wrapper

def bar():
    print('i am bar')

import time

#def timefun():
def timefun(func):

    print('3',func())
    def inner():
        a = time.time()
        print('a',a)
        print('inner_func',func())
        print('2')
        b = time.time()
        timeb = (b-a)*1000
        print('4')
        a = func()
        return a
    print('5')
    return inner
'''
'''
def timefun(func):
    a = time.time()
    func()
    b = time.time()
    timeb = (b-a)*1000
    #return func

@timefun   
def func():
    #print('1')
    time1 = time.time()
    print('time1',time1)
    return 2

if __name__ == '__main__':
    #fun()
    timefun(func)
'''

import time


def fool(foo):
    def inner():
        a1 = time.time()
        foo()
        b1 = time.time()
        print('b1-a1',(b1-a1))
        return foo
    return inner
'''
def fool(func):

    #print('3',func())
    def inner():
        a = time.time()
        print('a',a)
        print('inner_func',func())
        print('2')
        b = time.time()
        timeb = (b-a)*1000
        print('4')
        a = func()
        return a
    print('5')
    return inner

@fool
def foo():
    a = 3
    print('lala')
    return a

if __name__== '__main__':
    #foo()
    #fool(foo)
    foo()
'''

import time
def fool(foo):
    def inner(x,y):
        a1 = time.time()
        foo(x,y)
        #print(x+y)
        b1 = time.time()
        timeab = (b1-a1)*1000
        print(timeab)
        return foo
    return inner

@fool
def foo(x,y):
    print('i love lala')
    print('x',x)

@fool
def fo1(y,z):
    print('eilinge love lala')
    
if __name__=='__main__':
    foo('lala','eilinge')
    fo1('eilinge','lala')
