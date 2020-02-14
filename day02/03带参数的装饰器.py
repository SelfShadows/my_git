import time

Flag = True


def timmer_out(Flag):
    def timmer(func):
        def inner(*args, **kwargs):
            if Flag:  # 判断Flag是真是假
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                print(end - start)
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret
        return inner
    return timmer


# timmer=timmer_out(Flag)
# @timmer
@timmer_out(Flag)  # 先调用timmer_out(Flag)返回 timmer    在执行@timmer
def wahahha():
    time.sleep(0.1)
    print('wahahahahahhahahaho')


Flag = False


@timmer_out(Flag)
def adgai():
    time.sleep(0.1)
    print('adgaigaigaigaigi')


wahahha()
adgai()
