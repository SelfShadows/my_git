from multiprocessing import Event

e=Event()              #创建一个事件
print(e.is_set())      #查看一个事件的状态,默认为阻塞
e.set()                #将事件状态改为非阻塞：True
print(e.is_set())
e.clear()              #将事件状态改为阻塞：False
print(e.is_set())
print(123)
e.wait()               #根据阻塞状态来决定自己是否阻塞               wait  wait event set clear
print(456)






#set  和 clear
    #分别用来修改一个事件的状态 True或False
#is_set 用来查看一个事件的状态，默认设置为False,阻塞状态
#wait 是根据事件的状态来决定自己是否阻塞
    #False阻塞 True不阻塞