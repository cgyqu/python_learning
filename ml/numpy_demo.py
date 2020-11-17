#%%
import numpy as np

# %%
b = np.array([[1, 2], [3, 4]])
print(b)
# %%
dt = np.dtype([('age', np.int8)])
a = np.array([(10, ), (20, ), (30, )], dtype=dt)
print(a['age'])
print(a['age'][0])

# %%
a = np.arange(24)
print(a)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b)
print(b.ndim)
print(b.reshape(8, 3))
# zero数组
# %%
# 默认为浮点数
x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5, ), dtype=np.int)
print(y)

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

a = np.arange(15).reshape(3, 5)
print(a)
# 矩阵的形状
print(a.shape)
# 矩阵的位数
print(a.ndim)
# 元素的个数
print(a.size)
# 类型名称
print(a.dtype.name)
# %%
# 必须传入数组初始化
b = np.array([1, 2, 3, 4])
b

# %%
c = np.array([(1.5, 2, 3), (4, 5, 6)])
print(c.shape)
# %%
# zero :创建全为0的矩阵
z = np.zeros((3, 4))
print(z)
# %%
#range 测试
r = np.arange(10, 30, 5)
print(r)
# 由于浮点数精度问题，加入linspace函数
r = np.arange(0, 2, 0.2)
print(r)
# %%
l = np.linspace(0, 2, 9)
print(l)
# %%
# 最后一个轴从左到右打印，
# 倒数第二个从上到下打印，
# 其余部分也从上到下打印，每个切片用空行分隔。
r = np.arange(24).reshape(2, 3, 4)
print(r)
# %%
# 数组操作
a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = a - b
print(c)
# 平方
b = b**2
print(b)
s = 10 * np.sin(a)
print(s)
# %%
print(b < 2)
# %%
m1 = np.array(np.arange(1, 5, 1)).reshape(2, 2)
m2 = np.array(np.arange(6, 10, 1)).reshape(2, 2)
print(m1, m2)
print(m1 + m2)
# 相同位置元素相乘
print(m1 * m2)
# 矩阵相乘
print(m1 @ m2)
print(m1.dot(m2))
# %%
# 数组相关操作
arr = np.arange(12).reshape(3, 4)
print(arr.sum())
# axis = 0 代表按列计算
# axis = 1 代表按行计算
print(arr.sum(axis=0))
# %%
slice = np.arange(10)**3
#从开始到 index=6，隔一个替换元素
slice[:6:2] = -1000
print(slice[::-1])  # 倒序


# %%
def f(x, y):
    return 10 * x + y


indexArr = np.fromfunction(f, (5, 4), dtype=int)
print(indexArr)
print(indexArr[2, 3])
print(indexArr[1:3, :])
print(indexArr[-1])

# %%
# 改变形状
b = np.arange(24)
b.resize(4, 6)
print(b)
b.resize(6, 4)
print(b)
# %%
#随机取整
a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))
print(a)
print(b)
# 行叠加
c = np.vstack((a, b))
print(c)
# 列叠加
d = np.hstack((a, b))
print(d)

d2 = np.column_stack((a, b))
print(d2)
# %%
# 数组拆分
sp = np.floor(10 * np.random.random((2, 12)))
#拆分成3个数组
np.hsplit(sp, 3)
# 深拷贝，别的都是浅拷贝
cp = sp.copy()
cp[0, 0] = 1000
print(cp)
print(sp)
print(sp[[0, 1]])
# %%
import numpy as np
s1 = np.arange(12).reshape(3, 4)
print(s1)
i = np.array([
    [0, 1],  # indices for the first dim of a
    [1, 2]
])
#print(s1[i])
j = np.array([
    [2, 1],  # indices for the second dim
    [3, 3]
])
print(s1[i, :])
print(s1[i, j])
# %%
a = np.array([[1, 2]])
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0)
# %%
np.array([-1] * 10, dtype=int)
# %%
