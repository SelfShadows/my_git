from core.user  import User
from conf import setting
import json
import pickle
import os
import hashlib
def login(msg):
    print(msg)
    ret_md5=md5_password(msg['password'])
    with open(setting.userinfo,'r') as f:
        for line in f:
            name, password, path = line.split('|')
            if name==msg['username'] and password==ret_md5:
                return '登陆成功'
        else:
            return '用户名密码输入错误'

def register(msg):
    user_obj=User(msg['username'])   #记录用户的信息在内存里
    with open(setting.userinfo,'r') as f:
        for line in f:
            name,password,path=line.split('|')
            if name==msg['username']:
                return '用户名已存在'
    pickle_path=os.path.join(setting.pickle_path,msg['username'])

    with open(pickle_path,'wb') as f:
        pickle.dump(user_obj,f)
    os.mkdir(user_obj.home)      #创建属于这个用户的家目录

    md5=md5_password(msg['password']) #加密密码
    with open(setting.userinfo,'a') as f:
        f.write('%s|%s|%s\n'%(msg['username'],md5,pickle_path))
    return '注册成功'

def upload(msg):
    print(msg)


def download(msg):
    print(msg)


#加密方法
def md5_password(password):
    md5=hashlib.md5(bytes('li',encoding=setting.code))
    md5.update(bytes(password,encoding=setting.code))
    md5=md5.hexdigest()
    return md5


