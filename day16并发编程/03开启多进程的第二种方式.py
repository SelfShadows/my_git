from multiprocessing import Process
import os
class MyProcess(Process):
    def __init__(self,args1,args2):
        super().__init__()
        self.args1=args1
        self.args2=args2

    def run(self):
        print('子：',os.getpid())
        print(self.args1)
        print(self.args2)
if __name__=='__main__':
    print('主：',os.getpid())
    p1=MyProcess(1,2)
    p1.start()
    p2=MyProcess(3,4)
    p2.start()


#自定义类，继承Process类
#必须实现一个run方法，run方法中是子进程执行的代码