from core.socket_client import MySocketClient

class Auth:
    __instance=None
    def __new__(cls, *args, **kwargs):
        #单例模式
        if not cls.__instance:
            obj=object.__new__(cls)
            cls.__instance=obj
        return cls.__instance

    def __init__(self):
        self.socket=MySocketClient()
        self.username=None

    def login(self):
        username=input('请输入用户名:')
        password=input('请输入密码:')
        if username.strip()  and password.strip():
            self.socket.mysend({'username':username,'password':password,'operation':'login'})
        else:
            print('用户名，密码不能为空')
            return
        ret=self.socket.myrecv()
        print(ret)

    def register(self):
        while True:
            username=input('请输入要注册的用户名：')
            passworld1=input('请输入密码：')
            passworld2=input('请确认密码：')
            if username=='' or passworld1=='':
                print('用户名，密码不能为空')
            elif username.strip() and passworld1.strip() == passworld2.strip():
                self.socket.mysend({'username':username,'password':passworld2,'operation':'register'})
                ret=self.socket.myrecv()
                print(ret)
                return
            else:
                print('密码输入错误')


