
name = "小黑"


class Person():
    _ww = "ff"

    def __init__(self, name):
        self.name = name
        self.__bb = "bb"

    def _dream(self):
        print("{}在做梦".format(self.__bb))

    def __str__(self):

        return "{}".format(self.__bb)

p = Person("小李")
p._dream()
print(p)