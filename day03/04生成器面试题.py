

def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test()
for n in [1,10,5]:
    g=(add(n,i) for i in g)
#g=20,21,22,23
print(list(g))