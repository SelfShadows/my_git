import aa                #先写内置，在扩展，在自定义
import sys               #if__name__=='__main__'测试代码用的
import time as t   #给模块改名
from time import sleep
a=t.strftime('%Y-%m-%d %X')
print(aa.nihao())

def nihao():
    print(123)
print(aa.nihao())

print(sys.modules.keys())   #导入的模块先从modules.keys里找
print(sys.path)             #再从path里找