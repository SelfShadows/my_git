from abc  import abstractmethod,ABCMeta     #python中没有接口类有抽象类

class Walk_Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

class Swim_Animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass

class Fly_Animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(Walk_Animal,Swim_Animal):
    def walk(self):
        pass
    def swim(self):
        pass
class Oldying(Fly_Animal,Walk_Animal):
    def fly(self):
        pass
    def walk(self):
        pass
class Swan(Walk_Animal,Swim_Animal,Fly_Animal):
    def walk(self):
        pass
    def swim(self):
        pass
    def fly(self):
        pass

t=Tiger()
o=Oldying()
s=Swan()