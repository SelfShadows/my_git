from core.auth_client import Auth
def main():
    start_1=[('登陆','login'),('注册','register'),('退出','exit')]
    for i,item  in enumerate(start_1,1):
        print(item[0]+' 请按',i)
    while True:
        try:
            num=int(input('请输入您需要的操作>>>'))
            func_str=start_1[num-1][1]
        except:
            print('输入的信息有误,请输入1,2,3')
            continue
        if hasattr(Auth,func_str):
            auth_obj=Auth()
            func=getattr(auth_obj,func_str)
            ret=func()

            if ret: break
        elif auth_obj:
            auth_obj.socket.sk.close()
            exit()
        else:
            exit()


