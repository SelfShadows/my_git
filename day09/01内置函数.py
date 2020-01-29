class A:
    a = 1

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'haha'

    def __repr__(self):
        return '123'

    def __call__(self, *args, **kwargs):
        print('执行我了')
        for k in self.__dict__:
            print(k, self.__dict__[k])  # self.__dict__ 是个字典里面是类的全部属性


a = A('alex')
print(a)  # 执行str方法,没有str方法会执行repr方法
print('%s' % a)  # 同样执行str方法,没有str方法会执行repr方法

print('%r' % a)  # 执行repr方法
print(a.__repr__())  # 执行repr方法

a()  # 执行__call__方法  没有  call  方法会报错
