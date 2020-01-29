import pymysql


#增删改
conn=pymysql.connect(host='localhost',user='root',password='',database='db5')
cursor=conn.cursor()
user='xiaoli'
pwd='123123'
s1="insert into userinfo(name,password) values (%s,%s)"
r=cursor.execute(s1,(user,pwd))#执行SQL语句  #列表的方式
    #返回的r为受影响的行数
cursor.executemany(s1,[('laoxiao','123456'),('alex','112233')])#批量插入数据
conn.commit()#提交给SQL
    # 进行增删改都需要有这一步的操作
cursor.close()
conn.close()


