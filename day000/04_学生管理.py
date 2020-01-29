import os
file_name='store_xj.txt'
backup_file='backup'
def	r_file(file_name):
	if os.path.exists(file_name):
		f=open(file_name,'r')	
		while True:
			stu_str=f.readline()
			if stu_str == '':
				break
			else:
				stu_info_str=stu_str.split()
				student={'name':stu_info_str[0],'sex':stu_info_str[1],'agg':stu_info_str[2]}
				stus.append(student)
		f.close()

def w_file(file_name):
	if os.path.exists(file_name):
		if os.path.exists(backup_file):
			os.remove(backup_file)
		os.rename(file_name,'backup-'+file_name)
	f=open(file_name,'w')
	for student in stus:
		stu_str='%s\t%s\t%s\n'%(student['name'],student['sex'],student['agg'])
		f.write(stu_str)
	f.close()
def menu():
	print('='*50)
	print('学生管理系统'.center(44))
	print('增加学生请按      |1| ')
	print('删除学生请按      |2| ')
	print('修改学生请按      |3| ')
	print('查询学生请按      |4| ')
	print('查询全部学生请按  |5| ')
	print('退出请按          |6| ')
	print('='*50)
def id_stu(item):
	print('姓名:%s\t性别:%s\t年龄:%s'%(item['name'],item['sex'],item['agg']))

def del_stu(name):
	student=search_stu(name)
	if student==-1:
		return
	else:
		stus.remove(student)	
		print('删除成功')
	

def add_stu():
	name=input('请输入学生姓名:')	
	sex=input('请输入学生性别:')	
	agg=input('请输入学生年龄:')	
	stu={}
	stu["name"]=name
	stu['sex']=sex
	stu['agg']=agg
	stus.append(stu)
	print('添加成功')


def search_stu(name):
	for i in stus: 
		if i['name']==name.strip():
			id_stu(i)
			return i
	else:
		print('没有这个学生')
		return -1
def show_stu():
	print('序号\t名字\t性别\t年龄') 
	for b,i in enumerate(stus,1):
		print("%s\t\t%s\t\t%s\t\t%s"%(b,i['name'],i['sex'],i['agg']))

def change_stu(name):
	i=search_stu(name)
	if i==-1:
		return
	else:
		i['name']=input('请输入姓名：')
		i['sex']=input('请输入性别：')
		i['agg']=input('请输入年龄:')
		print('修改成功')

stus=[]
menu()
r_file(file_name)
while True:
	a=input('输入想要的操作:')
	if a=='1':
		add_stu()
		w_file(file_name)
	elif a=='2':
		name=input('请输入要删除的姓名:')
		del_stu(name)
		w_file(file_name)
	elif a=='3':
		name=input('请输入要修改的姓名')
		change_stu(name)		
		w_file(file_name)
	elif a=='4':
		name=input('请输入查询的名字')
		search_stu(name)	
	elif a=='5':
		show_stu()	
	elif  a=='6':
		break	
