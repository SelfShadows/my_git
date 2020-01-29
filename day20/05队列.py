import queue
#q.put()
# q.get()
# q.put_nowait()        #把值放入队列中，队列满了会报错
# q.get_nowait()        #从队列中取值，队列中没有值会报错

q1=queue.Queue(3)  #队列先进先出
q1.put(1)
q1.put(2)
q1.put(3)
print('quequ.Queue')
print(q1.get())
print(q1.get())
print(q1.get_nowait())
print('-'*50)

q2=queue.LifoQueue()     #栈   后进先出
q2.put(1)
q2.put(2)
q2.put(3)
print('quequ.LifoQueue')
print(q2.get())
print(q2.get())
print('-'*50)

q3=queue.PriorityQueue()     #优先级队列 越小越优先，优先级一样，用ascll码排
q3.put((4,'213'))
q3.put((10,'b'))
q3.put((5,'aa'))
print('quequ.PriorityQueue')
print(q3.get())
print(q3.get())