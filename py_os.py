# os提供管理文件和文件夹的方法
#%%
import os

isExist = os.access('data.bat',os.F_OK)
print(isExist)
print(os.getcwd())
os.chdir("./data")
print(os.getcwd())
# %%
APP_DIR = os.path.dirname(__file__)
base_dir = os.path.dirname(APP_DIR)

print(APP_DIR)
print(base_dir)
# %%
