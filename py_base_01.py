# -*- coding: utf-8 -*-
# print 注释
print("123")
'''
这里是多行注释操作
'''

# if else预发
isPrint = True

if isPrint:
    print(isPrint)
else:
    print(False)

# 多行代码
num1 = 10
num2 = 100
num3 = 1000
total = num1 + \
    num2 + \
    num3
print(total)

# 数组不需要换行

arr = [1,2,3,
       4,5,6]
print(arr)

'''
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''
# python中单引号和双引号使用完全相同。
str1 = "123"
str2 = '456'
print(str1,str2)
# 字符串操作
str3="123456789"
print(str3[0])
print(str3[2:5])
print(str3[2:])
print(str3[2:-1])
print(str3*2)
print("hello\nworld!")
# 开始加r标识不进行转义字符串
print(r"hello\nworld!");

# 单行代码
print(1);print(2);


'''
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *
'''