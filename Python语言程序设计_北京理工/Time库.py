import time
print(time.time()) #时间戳 浮点数

print(time.ctime()) #人类可读时间

print(time.gmtime()) #计算机可读时间


print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))


