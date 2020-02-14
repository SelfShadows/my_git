class Stack(object):

    def __init__(self):
        self.data = []

    def __str__(self):
        return '%s' % self.data

    def push(self, val):
        return self.data.append(val)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]


# a = [1, 2, 45, 435, 6453, 234]
# ret = a.insert(0, 22)  # 在下标为0 里插入22
a = Stack()
a.push([1, 3, 4])
a.push("xiaoli")
a.push("xiaohei")
print(a)
print(a.top())

