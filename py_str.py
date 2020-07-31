# -*- coding: utf-8 -*-
# 字符串格式化操作
# 多行注释，其实是字符串
'''
测试1
'''
str = '''thisisisistest is test
'''
print(str)
# 首字母大写
print("hello".capitalize())
# 字符串截取操作,不包括最后面字符
# 长度为end-start
print(str[1:5])
print(str[0:5])
print("endswith:", str.endswith('\n'))
# find不会报异常.index报异常
print("str find test:", str.find('test'))
print("str find test1:", str.find('test1'))
print("str index test:", str.index('test'))

try:
    print("str index test1:", str.index('test1'))
except Exception:
    print("出错了")
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True
print("test".isalnum())
print('123'.isalnum())
print("test ".isalnum())
# isalpha() 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True
print("test".isalpha())
print("测试".isalpha())

# 纯数字判断
print('123'.isdigit())
print("test ".isdigit())
#isspace 如果字符串中只包含空白，则返回 True，否则返回 False.
print(" ".isspace())
print("".isspace())
print("test".isspace())

print("as".join(('1','2','3')))
print(len("test"))
print(" test".lstrip())
print("test ".rstrip())
print("TEST".lower())
print("I    am  jemmy".split()[1:3])

repr("123")
import math
for i in range(1,11):
    print("{0:2d}{1:3d}{2:4d}".format(i,i**2,i**3))

num = 1
print(f"{num + 1}")