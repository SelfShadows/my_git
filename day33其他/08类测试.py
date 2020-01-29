
class Persen():

    def __init__(self, name, sex, age=10):
        self.name = name
        self.sex = sex
        self.age = age
        print(name, sex, age)

    def run(self):
        print(self.name)

    @property
    def start(self):
        return self.sex

a1 = Persen(1, 2)
a1.run()
# print(a1.start())
print(a1.start)