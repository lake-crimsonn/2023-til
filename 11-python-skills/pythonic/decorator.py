"""
    decorator
    데코레이터는 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용합니다.
"""


# 기능이 반복되는 함수를 여러개 만들 때 사용한다.


def hello():
    print('hello 함수 시작')
    print('hello')
    print('hello 함수 끝')


def world():
    print('world 함수 시작')
    print('world')
    print('world 함수 끝')


hello()
world()


# 함수를 매개변수로 받고, wrapper에서 함수를 실행하고, wrapper를 반환한다.


def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작2')
        func()
        print(func.__name__, '함수 끝2')
    return wrapper


def hello():
    print('hello2')


def world():
    print('world2')


trace_hello = trace(hello)()
trace_world = trace(world)()


# @ 데코레이터 사용하기
# hello()와 world() 위에 @trace를 써줌으로써 hello와 world를 매개함수로 사용한다.


def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작3')
        func()
        print(func.__name__, '함수 끝3')
    return wrapper


@trace
def hello():
    print('hello3')


@trace
def world():
    print('world3')


hello()
world()


# @ 데코레이터는 여러개를 지정해서 사용할 수 있다.


def deco1(func):
    def wra():
        print('deco 1')
        func()
    return wra


def deco2(func):
    def wra():
        print('deco 2')
        func()
    return wra


@deco1
@deco2
def hello():
    print('hello4')


hello()
