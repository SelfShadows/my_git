class FooStart(object):

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '%s'%self.my_list

    def push(self, msg):
        ret = self.my_list.append(msg)
        return ret

    def pop(self):
        ret = self.my_list.pop()
        return ret


a = [1, 2, 45, 435, 6453, 234]
# ret = a.insert(0, 22)  # 在下标为0 里插入22
a = FooStart(a)
a.push([1,3,4])
print(a)
a.pop()
print(a)
