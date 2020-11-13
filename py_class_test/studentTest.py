# -*- coding: utf-8 -*-
from student import Student 
from zhangsan import ZhangSan

'''
类测试及定义
'''
stu = Student('test',29,10)
print(stu.sayHello())
print(stu.getage())
print(stu.getname())

zhangsan = ZhangSan('zs',29,10,'A')
print(zhangsan.sayHello())
print(zhangsan.getGrade())
zhangsan.getFlag()

import builtins
dir(builtins)

if True:
    msg = "scode test"
print(msg)


total = 0 # 这是一个全局变量
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
# 可写函数说明
def sum( arg1, arg2 ):
    global total
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
sum(10,20)
print(total)
