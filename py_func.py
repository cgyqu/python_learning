def test(name):
    print("from method", name)


test("hello")


def printinfo(name, age=18):
    print(name, age)


printinfo("cgy")

# 单个*号参数以数组传入


def uncertainLength(name, *args):
    for x in args:
        print(x, end=",")
    print(name, len(args))


uncertainLength("cgy", 10, 20, 30)

# ** 2个星号参数以dict传入

def uncertDict(name, **argdict):
    print(argdict['a'])
    print(name, argdict)


uncertDict("cgy", a=1, b=2)

# 单个*后的参数必须用关键词传入

def f(a, b, *, c):
    return a + b + c

# 这样写会报错f(1,2,3)
print(f(1,2,c=3))

def f1(*,a,b,c):
    return a + b+ c

print(f1(a=1,b=2,c=3))

# lambda 表达式，好搓
sum = lambda a,b:a+b

sum(1,2)