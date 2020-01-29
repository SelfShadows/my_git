"""
importlib 模块
"""

# from xx import oo
# print(oo.name)

import importlib
o = importlib.import_module("xx.oo")
print(o.name)
# a = o.Person('小李')
# a.dream()

# 用字符串找函数 类 利用 反射
ret = getattr(o, "Person")
a = ret("小李")
a._dream()
