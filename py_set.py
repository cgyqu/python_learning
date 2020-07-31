# list
list = [1, 2, 3, 4, 5]
list.insert(6, "test")
print(len(list))
print(list.pop())

# 字典
dict = {'name': '123'}
print(dict['name'])
isIn = 'name' in dict
print(isIn)


# 元祖
tuple = (1, "2", 3)
print(tuple[0:3])
print(tuple[1:])
print(tuple[-1:])
id(tuple)


# Set，无序不重复的集合
set = {1, 2, 3, 4}
set1 = {4, 5, 6}
set.update(set1)
set.discard(1)
set.discard(7)
set.remove(7)
print(len(set), set)

# iter
list = [1, 2, 3, 4]
list.append(5)
list.insert(0, 0)
print(list.pop())
print(list)
it = iter(list)
for x in it:
    print(x)
# 迭代
list1 = [1, 2, 3]

list2 = [3*x for x in list1]
print(list2)

list3 = [3*x for x in list1 if x > 1]
print(list3)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

list4 = [[row[i] for row in matrix] for i in range(4)]
print(list4)
t = 1,2,34
print(t)

if 1 in t:
    print("1 in t")

l1 = [1,2,3]
l2 = ['bar','foo','baz']
z = zip(l1,l2)
print(type(z))
print(z)
for a,b in z:
    print(a , b)

basket =['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
sets = set(basket)
print(sets)
