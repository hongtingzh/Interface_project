from functools import wraps


def function2(func):
    """
    无参的函数构造器
    :return:
    """
    @wraps(func)
    def wraps_func(*args, **kwargs):
        print('开始执行：' + function1.__name__)
        func(*args, **kwargs)
        print('执行结束：' + function1.__name__)
    return wraps_func


def function3(arg=True):
    """
    有参数的函数构造器
    :param arg:
    :return:
    """
    def inner_func(func):
        @wraps(func)
        def wraps_func(*args, **kwargs):
            print('开始执行：' + function1.__name__) if arg else print('.......')
            func(*args, **kwargs)
            print('执行结束：' + function1.__name__)
        return wraps_func
    return inner_func


@function3(False)
def function1():
    print('正在执行：' + function1.__name__)

# @function2 ===> function2(function1) ==返回结果==> wraps_func  函数对象
# function1() ==执行==> wraps_func()


function1()