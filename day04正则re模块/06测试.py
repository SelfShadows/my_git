import re

a='1 - 2 * ( ( 60-30  +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

# print(eval(a))
cont=0
new_a=a.replace(' ','')
print(eval(a))
