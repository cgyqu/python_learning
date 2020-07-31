import json
import requests

class httprequest:
    @staticmethod
    # get request
    def sendGet(url, header):
        responseGet = requests.get(url, headers=header)
        # return as json string
        return responseGet.text
    @staticmethod
    # post reguest
    def sendPostwithHeaders(url, header, body):
        postRes = requests.post(url, headers=header, data=body.encode('utf-8'))
        print(postRes)
        # return as json string
        return postRes.text
