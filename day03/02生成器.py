

def generator():
    a='qwertyyui'
    b='12345678'

    for i in a:
        yield i
    #     ||
    #     ||
    yield from b   

g=generator()
for i in g:
    print(i)