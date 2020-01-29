import hashlib

with open('userinfo','w') as f:
    user=input('请输入用户名:')
    passwrld=input('请输入密码:')
    md5=hashlib.md5()
    md5.update(bytes(passwrld, encoding='utf-8'))
    f.write(user+'|')
    f.write(md5.hexdigest())

# u1='1234567890-'
# a=hashlib.md5()
# a.update(bytes(u1,encoding='utf-8'))
# print(a.hexdigest())

# user=input('请输入用户名:')
# passwrld=input('请输入密码:')
# with open('userinfo') as f:
#     for line in f:
#         u1,p1=line.split('|')
#         print(u1,p1)
#         md5=hashlib.md5()
#         md5.update(bytes(passwrld,encoding='utf-8'))
#         md5_pwd=md5.hexdigest()
#         print(md5_pwd)
#         if u1==user and md5_pwd==p1:
#             print('登陆成功')

