import struct

ret=struct.pack("i",6600)  #'i'表示int,把数字转换成固定长度的bytes类型
print(ret)