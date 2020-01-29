
def jilu(func):
    def inner(*args,**kwargs):
        with open('jilu','a',encoding='utf-8') as f:
            f.write(func.__name__+'\n')
        ret=func(*args,**kwargs)
        return ret
    return inner
@jilu
def shoplist_add():
    print('增加一件物品')
@jilu
def shoplist_del():
    print('删除一件物品')

shoplist_add()
shoplist_del()

print(shoplist_add.__name__)

