# -*- coding: utf-8 -*-
import time
import json
import requests

mvurl = []
mvurl.append("http://tcwlservice.qa.17usoft.com/livechat/admin/roleData/addLabel")
mvurl.append("http://tcwlservice.qa.17usoft.com/livechat/admin/roleData/addProductLabel")
mvurl.append("http://tcwlservice.qa.17usoft.com/livechat/admin/roleData/addRole")
mvurl.append("http://tcwlservice.qa.17usoft.com/livechat/admin/roleData/addRoleMeau")
mvurl.append("http://tcwlservice.qa.17usoft.com/livechat/admin/roleData/addRoleUser")



# get request
def sendGet(url,header):
    responseGet = requests.get(url,headers = header)
    return responseGet.text

# post reguest
def sendPostwithHeaders(url,header,body):
        postRes = requests.post(url, headers=header, data=body.encode('utf-8'))
        return postRes.text

def execute(url):
    time_start = time.time()
    print('迁移地址：' + x)
    header = {'Content-Type': 'application/json','Cookie':'access_token=5acc9d471cf842bd7d5f1a216b811ec2;' }
    res = sendGet(x,header)
    time_end = time.time() 
    print("迁移执行结果:{0},耗时:{1}ms".format(res, time_end - time_start))

for x in mvurl:
   execute(x)

print('数据迁移完成')

input("Press Enter key to exit.")



