
# -*- coding: utf-8 -*-
counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = "中文测试"     # 字符串
print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
print(a,b,c)

'''
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
'''

# number
'''
type 获取类型
isinstance 判断是否为某个类型的实例
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(type(a) == int)
isinstance(a, int)

# 除法
print(2 / 4)
print(2 // 4)
print(5 / 2)
print(5 // 2)
print(2 ** 30)


## list操作
list = ['abcd',1234,2.23,'test',70.2,1]
list1 = [1,2,3]
print(list)
print(list[0])
print(list[0:3])
print(list[0:-1])
print(list * 2)
print(list + list1)

list2 = [1,2,3,4,5]
list2[0:1] = []
print(list2)
print(list2[0:4:3])


word = "123 456 789"
words = word.split(" ")
end = -1 * (len(words) + 1)
print(end)
words = words[-1::-1]
print(words)

## 元组
tuple = (1,2,3,"a","b",7.0)
print(tuple[0])
print(tuple[0:2])
tuple[0] = 1

### dict
dict = {}
dict["name"] = 'cgymy'
dict["id"] = 1
print(dict['id'])
print(dict)
print(dict.keys)
print(dict.values)

num = 2
num**=10
print(num)
a = 4
b = 5
print(a & b)
print(a | b)
print(2 >> 1)
print(2 << 5)
print(2 << 5)

### and or not
if a and b :
    print(a + b)
a = 0
if a and b : 
    print(a,b)
else :
    print(a)
if a or b:
    print(a,b)

if not (a and b):
    print(a ,b)

## in not in
a1 = 1
b1 = 5
list = [1,2,3,4,5]
print(a1 in list)
print(b1 not in list)

'''
is 标识两个类型和值相同
'''
print(a1 is not b1)
b1 = 1
print(a1 is b1)

### 下面数字xjb转换
x = '1'
print(int(x))
print(float(x))
print(str(1))
print(complex(x))


