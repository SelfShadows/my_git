flag=False
def rz(func):
    def inner(*sargs,**wksargs):
        global flag
        if flag:
            ret = func(*sargs, **wksargs)
            return ret
        else:
            username=input('请输入用户名：')
            password=input('请输入密码：')
            if username=='li' and password=='123':
                flag = True
                print('登陆成功')
                ret=func(*sargs,**wksargs)
                return ret
            else:
                print('登陆失败')
    return inner



@rz
def shoplist_add():
    print('增加一件物品')
@rz
def shoplist_del():
    print('删除一件物品')


shoplist_add()
shoplist_del()