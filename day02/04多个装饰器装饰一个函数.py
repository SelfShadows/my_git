def test1(func):  # func==>wahaha
    def inner1(*args, **kwargs):
        print('执行1111111')
        ret = func(*args, **kwargs)  # wahaha
        print('执行2222222')
        return ret

    return inner1


def test2(func):  # func-->inner1
    def inner2(*args, **kwargs):
        print('执行3333333')
        ret = func(*args, **kwargs)  # inner1
        print('执行4444444')
        return ret

    return inner2


def test3(func):  # func-->inner1
    def inner2(*args, **kwargs):
        print('执行5555555')
        ret = func(*args, **kwargs)  # inner1
        print('执行6666666')
        return ret

    return inner2


@test3
@test2  # wahaha=test2(wahaha)-->test2(inner1)=inner2
@test1  # wahaha=test1(wahaha)=inner1()
def wahaha():  # 先执行@test1,在执行@test2
    print('哇哈哈')


wahaha()  # ==>inner2

#      test2 上下包住test1 ,test1上下包住 wahaha
