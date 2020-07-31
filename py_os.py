# os提供管理文件和文件夹的方法
import os

isExist = os.access('data.bat',os.F_OK)
print(isExist)
print(os.getcwd())
os.chdir("./data")
print(os.getcwd())