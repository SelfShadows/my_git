

class Person():
    _ww = "ff"
    DEBUG = True
    TEXT = False

    def __init__(self, name):
        self.name = name
        self.__bb = "bb"

    def _dream(self):
        print("{}在做梦".format(self.__bb))

    @property
    def RUN(self):
        print('run起来了')
        return "返回值"

    def __str__(self):

        return "{}".format(self.__bb)

