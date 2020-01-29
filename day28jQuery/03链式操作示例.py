'''
链式操作示例
'''

class dog():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def wang(self):
        print('旺旺')
        return self     #需返回本身就可以支持链式操作
    def run(self):
        print('哒哒``哒哒')
        return self
f=dog('xiaoqiang',9000)
f.run().wang().run()

