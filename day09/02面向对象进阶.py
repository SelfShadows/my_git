from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])  # rank 牌面大小，suit 花色
c1 = Card(2, '红心')
print(c1)
print(c1.suit)  # 相当于定义了个类，只有属性没有方法
