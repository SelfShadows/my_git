class Base(object):

    def func(self):
        print('Base.func')


class Foo(Base):

    def func(self):
        # 方式一: 根据mro的顺序执行方法
        super(Foo, self).func()
        # 方式二: 主动执行Base类的方法
        Base.func(self)
        print('Foo.func')


obj = Foo()
obj.func()
print(Foo.__mro__)


# 特殊方法__getattr__/__setattr__注意事项：

class Aa(object):
    def __init__(self):
        # self.storage = {}
        object.__setattr__(self, 'storage', {})  # 执行object类的__setattr__方法 并给 对象.storage 赋值了一个空字典

    def __setattr__(self, key, value):
        self.storage[key] = value
        print(key, value, self.storage)


obj = Aa()
obj.xx = 123
