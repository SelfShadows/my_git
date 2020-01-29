"""
两种单例模式
"""
print('只保存最后一个单例对象'.center(80, "*"))


class Person(object):
    __instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


p1 = Person("小李")
p2 = Person("老肖")
p3 = Person("alex")
print(p1==p2)
print(id(p1), id(p2))
print(p1.name, p2.name, p3.name)

print('只保存第一个单例对象'.center(80, "*"))


class Person2(object):
    __instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls,name):
        if not cls.__instance:
            cls.__instance = Person2(name)
        return cls.__instance


p1 = Person2.get_instance("小李")
p2 = Person2.get_instance("老肖")
p3 = Person2.get_instance("alex")
print(p1==p2)
print(id(p1), id(p2))
print(p1.name, p2.name, p3.name)