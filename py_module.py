import common
from common import printerror,printinfo
import sys

print(sys.path)

common.printinfo("this is info")
common.printerror("this is error")
printinfo("this is info")
printerror("this is error")

dir(common)
dir()