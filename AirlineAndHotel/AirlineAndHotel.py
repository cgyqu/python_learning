# -*- coding: gb2312 -*- 
fo = open("E:/data.txt","r")
str = fo.read()
print(str)
fo.close()

try:
    with open("E:/data.txt","w") as f:
        f.write("this is a test")
except IOError as e:
    print(e)
except TypeError as te :
    print(te)

