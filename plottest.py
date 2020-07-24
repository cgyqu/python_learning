#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 
# %%
x = np.arange(0,9,0.1)
y = np.sin(x)
y1 = np.cos(x)
plt.title("y=xin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,"-b",x,y1,"-r")
plt.show()

# %%
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
plt.hist(a, bins =  [0,20,40,60,80,100]) 
plt.title("histogram") 
plt.show()

# %%
plt.rcParams['font.family']=['STFangsong']
x = np.arange(0,3* np.pi,0.1) 
y = np.sin(x) #2  * x +  5 
plt.title("测试") 

plt.xlabel("x") 
plt.ylabel("y") 
plt.plot(x,y,"-r") 
plt.show()

# %%
