import functools

def index(a,b):
    return a+b

# 原来的调用方法
ret = index(3,1)
print(ret)

# 偏函数, 帮助开发者自动传递参数
new_func = functools.partial(index, 55)
ret = new_func(1)
print(ret)