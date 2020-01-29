'''
问执行完下面代码后,l,m的内容分别是什么
'''
def func(m):
    for k, v in m.items():
        m[3] = v + 2

m = {1: 2, 3: 4}
l = m  # 浅拷贝 l和m指向一个内存地址，l和m会一起改变
from copy import deepcopy
l2 = deepcopy(m)       # 深拷贝 l2和m就没有关系了
l2[90] = 100
l[9] = 10
func(l)
m[7] = 8
print(m, l, l2)
# 1.在python中遍历字典的时候不能对字典本身做涉及键的操作(key不能修改)
# 2.深浅拷贝的理解


# 枚举
a = [1, 2, 34, 2, 3, 22, 2, 3]
for k, v in enumerate(a):
    print(k + 1, v)
