"""
importlib 模块
"""
import importlib

# 用字符串找函数 类 利用 反射
aa = ("xx.settings.Person")
p, c = aa.rsplit('.', maxsplit=1)
m = importlib.import_module(p)
cls = getattr(m, c)
ret = cls("xiaoli")

# 获取类的所有静态字段
for key in dir(cls):
    if key.isupper():  # 如果key 是大写
        if key == "RUN":
            print(key, getattr(ret, key))
            continue
        print(key, getattr(cls, key))

