
# 读取内容 r 读取模式
# encoding="utf-8"  解决读取文件内容时，中文乱码问题
f = open("test.txt",'r',encoding="utf-8")

# 读取文件全部内容
# c = f.read()
# print(c)

# 按行读取文件全部内容
# lines = f.readlines()
# print(lines)

# 一次读取一行内容
line = f.readline()
print(line)
f.close()