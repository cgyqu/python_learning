# -*- coding: utf-8 -*- 

import requests


def sendhttp():  
    headers = {"Content-type": "application/x-www-form-urlencoded",  
               "Accept": "text/plain"}  
    res = requests.get("http://www.baidu.com",headers)
    return res

res = sendhttp()  

print(res.status_code)
print(res.cookies)
print(res.ok)
print(res.text)


