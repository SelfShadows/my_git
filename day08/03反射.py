import sys
# hasattr   getattr  delattr  setattr
eval('print(123)')  # 也可以处理字符串但是存在安全隐患 而反射就解决了安全问题
# 反射 ： 是用字符串类型的名字去操作 变量


class Teacher:
    dic={'k1':'1','k2':'2'}
    @classmethod
    def func(cls):
        print('哇哈哈')


if hasattr(Teacher,'dic'):      # hasattr 有这个字符串返回True,没有返回False
    a=getattr(Teacher,'dic')    # getattr获取这个字符串，这两个内置函数一般搭配使用
    print(a)                        # 类.属性
c = getattr(Teacher,'func')    # 类.方法
c()
# 可以从字符串中取值


def qqxing():
    print('qqxing')


if hasattr(sys.modules['__main__'],'qqxing'):
    a=getattr(sys.modules['__main__'],'qqxing')# 反射自己的模块
    a()
# sys.modules['__main__'] 自己的文件
