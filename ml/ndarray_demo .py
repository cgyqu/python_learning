# 说明# ,构造函数
# 名称	描述
# object	数组或嵌套的数列
# dtype	数组元素的数据类型，可选
# copy	对象是否需要复制，可选
# order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
# subok	默认返回一个与基类类型一致的数组
# ndmin	指定生成数组的最小维度
#%%
import numpy as np 
a = np.array([1,2,3])  
print (a)
# %%
b = np.array([[1,  2],  [3,  4]])  
print (b)
#%%
dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a['age'])
print(a['age'][0])


# %%
a = np.arange(24)  
print(a)
print(a.ndim)             # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print(b)
print(b.ndim)
print(b.reshape(8,3))
# zero数组
# %%
# 默认为浮点数
x = np.zeros(5) 
print(x)
 
# 设置类型为整数
y = np.zeros((5,), dtype = np.int) 
print(y)
 
# 自定义类型
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)
# %%
