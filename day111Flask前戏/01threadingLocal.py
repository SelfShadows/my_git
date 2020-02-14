"""
Flask 的 Local对象实现
"""

import time
import threading

try:
    import greenlet
    get_ident = greenlet.getcurrent  # 获取携程ID
except Exception as e:
    get_ident = threading.get_ident  # 获取进程ID


class Local(object):
    DIC = {}

    def __getattr__(self, item):
        ident = get_ident()
        if ident in self.DIC:
            return self.DIC[ident].get(item)
        return None

    def __setattr__(self, key, value):
        ident = get_ident()
        if ident in self.DIC:
            self.DIC[ident][key] = value
        else:
            self.DIC[ident] = {key: value}


# obj = threading.local()  # Django threading模块自带的
obj = Local()  # 增强版， 可以对携程开辟空间

def task(i):
    obj.xxx = i
    time.sleep(1)
    print(obj.xxx)


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()
