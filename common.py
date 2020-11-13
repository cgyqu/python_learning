import sys
import math
print(sys.argv)
print(math.log(1024,2))

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print("from import")

sys.exit()

def printinfo(msg):
    print("info:", msg)
def printerror(msg):
    print("error:", msg)


