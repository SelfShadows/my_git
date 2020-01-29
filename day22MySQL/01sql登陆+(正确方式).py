import pymysql
user=input('username:')
pwd=input('password:')

conn=pymysql.connect(host='localhost',user='root',password='',database='userinfo')#与数据库建立连接(打开柜子)
cursor=conn.cursor()#光标，指针,游标(用手去拿)
s1="select * from info where username=%s and password=%s"
cursor.execute(s1,[user,pwd])#执行SQL语句  #列表的方式
# s1="select * from userinfo where name=%(u)s and password=%(p)s"
# cursor.execute(s1,{'u':user,'p':pwd})#执行SQL语句  #字典的方式

result=cursor.fetchone()#执行SQL语句拿到一条返回结果

cursor.close()#关闭光标
conn.close()#关闭连接uu

if result:#result 有值
    print('登陆成功')
else:    #result 没有值
    print('登陆失败')

