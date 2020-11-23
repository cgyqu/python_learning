#%%
from utils import common
print(common.base_dir)

num = 1
num1 = 2
def fun1():
    global num
    global num1
    num1 = 0
    num += 1
    num1 += 5

fun1()
print(num)
print(num1)

# %%
def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()
# %%
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# %%
