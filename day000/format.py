data = {"name": "Q1mi", "age": 18}
a="Name:{name}, Age:{age}".format(**data)
print(a)

b="{:,}".format(1234567890)
print(b)