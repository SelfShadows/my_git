
#只要含有yield关键字的函数都是生成器函数
#yield不能和return共用且需要写在函数内

def generator():
    for i in range(20000):
        yield '哇哈哈%s'%i

w=generator()
a=0
for i in w:
    a+=1
    print(i)
    if a>50:
        break

b=w.__next__()
print(b)