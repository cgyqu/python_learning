# -*- coding: gb2312 -*- 
import time;

list = ['1', 2, 3]
print(list[0])
print(len(list))
tup1 = ('physics', 'chemistry', 1997, 2000);
print(tup1[0])
print(len(tup1))


def formattime(format) :
    if format == '' :
        return;
    timess =time.strftime(format)
    print(timess)

format = '%Y-%m-%d %H:%M:%S'
formattime(format)

