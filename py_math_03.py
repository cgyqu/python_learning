# -*- coding: utf-8 -*-
import math
import random
import string

print(5 // 2)
print(5 / 2)

print(abs(-2))
#往上取整数
print(math.ceil(4.1))#5
# 往下取整
print(math.floor(4.9))#4
print(math.exp(1))
print(math.fabs(-10.0))
print(math.log(100,10))

print(range(5))
print(random.choice(range(5)))



## choice 从给定序列中随机选一个出来
def getpasswd(length):
    b = string.digits + string.ascii_letters + string.punctuation
    pwd =''
    for i in range(0,length):
        pwd += random.choice(b)
    return pwd

print(getpasswd(20))

# randrange([start],stop,[step])
# 随机0到stop-1个数之间的任意一个
print(random.randrange(100))
# 随意一个奇数，1+2*n
print(random.randrange(1,100,2))
print(random.randrange(0,100,2))
print("hello".capitalize())
print("hello".center(10,'0'))
print("".join(('1','2','3')))




