import pymysql
import random
import time

def timmer(f):           #装饰器函数
    def a(*args,**kwargs):   #可以传任何参数，*代表多个参数，**代表按关键字传参
        start=time.time()
        q=f(*args,**kwargs)              #被装饰的函数
        end=time.time()
        print(end-start)
        return q            #相当于返回func()的return '新年好'
    return a
@timmer
def func():
    conn=pymysql.connect(host='localhost',user='root',password='',database='db5',charset='utf8')
    cursor=conn.cursor()
    a=1
    for i in range(1000000):
        b=random.randint(100000,100000000)
        c=random.choice(['男','女'])
        a1='alex'+str(a)
        b1=str(b)+'@qq.com'
        sql="insert into userinfo2(name,email,gender) values(%s,%s,%s)"
        cursor.execute(sql,[a1,b1,c])
        a+=1
    conn.commit()

    cursor.close()
    conn.close()

func()