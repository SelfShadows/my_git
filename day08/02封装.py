class Person:
    __key=123
    def __init__(self,name,paswd):
        self.name=name
        self.__paswd=paswd

    def __pwd(self):
        return self.__paswd

    def pay(self):
        aa=self.__paswd
        print(self.__pwd())
        print(aa)
a=Person('li',333)
print(a._Person__pwd())  #_类名__属性名或方法名   #外部调取私有属性