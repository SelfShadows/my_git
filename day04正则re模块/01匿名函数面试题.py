

# aa={'k1':1231,'k2':456,'k3':12123,}
# print(min(aa,key=lambda k: aa[k] ))
# print(aa['k1'])

a=('a','b')
b=('c','d')
# def func(a):
#     return {a[0]:a[1]}
c=zip(a,b)
print(c)
# d=map(func,c)
d=map(lambda c:{c[0]:c[1]},c)
for i in d:
    print(i)




