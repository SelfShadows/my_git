# 可变对象不能做关键字参数
def func(arg, li=[]):
    li.append(arg)
    return li

l1=func(21)
l2=func(21,[1,])
l3=func(28)

print(l1)
print(l2)
print(l3)


list5=[11,22,33,44,55]
# 打乱列表顺序
import random
random.shuffle(list5)
print(list5)

