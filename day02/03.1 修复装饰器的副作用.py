from functools import wraps

def timmer(func):
    @wraps(func)  # 修复装饰器带来的副作用 （记录日志很有用）
    def inner(*args,**kwargs):
        print('hello')
        ret=func(*args,**kwargs)
        print('world')
        return ret
    return inner
@timmer
def func():
    '''
    这个函数是个测试装饰器的函数
    :param name: 接收一个字符串类型的值
    :return: 打印一句话
    '''
    print('小李')
func()
print(func.__doc__)
print('__name__=',func.__name__)