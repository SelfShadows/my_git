# 饰器形成过程：最简单的装饰器 有返回值的 有一个参数的  万能参数的

import time
from functools import wraps


# 装饰带多个参数函数的装饰器
def timmer(f):  # 装饰器函数
    # @wraps(f)
    def a(*args, **kwargs):  # 可以传任何参数，*代表多个参数，**代表按关键字传参
        start = time.time()
        q = f(*args, **kwargs)  # 被装饰的函数
        end = time.time()
        print(end - start)
        return q  # 相当于返回func()的return '新年好'

    return a


@timmer  # 语法糖  @装饰器函数名
def func1(b, c):  # 被装饰的函数
    time.sleep(1)
    print('大家好', b, c)
    return '新年好'


print(func1.__name__)

# @timmer                 #语法糖  @装饰器函数名
# def func2(b):             #被装饰的函数
#     time.sleep(1)
#     print('大家好',b)
#     return '新年好'
# func=timmer(func)      这一行相当于  @timmer
ret1 = func1(1, c=7)  # 相当于执行a()并返回q给ret
print(ret1)  # 打印func的返回结果
# ret2=func2(3)
# print(ret2)
# 装饰器的作用————不想修改函数的调用方式，但是还想在原来的函数前后添加功能
# timmer就是一个装饰器函数，只是对一个函数有一些装饰作用

# 原则：  开放封闭原则
# 开放：  对扩展是开放的
# 封闭：  对修改是封闭的

# 本质:   闭包函数

# #封板
#  #                                             装饰器的固定模式
# def wrapper(f):                     #装饰器函数，f是被装饰的函数
#     def inner(*args,**kwargs):
#         '''在被装饰函数之前要做的事'''
#         ret=f(*args,**kwargs)
#         '''在被装饰函数之后要做的事'''
#         return ret
#     return inner
# @wrapper           #func=wrapper(func)
# def func():
#      print(123)
