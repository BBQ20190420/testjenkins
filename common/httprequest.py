import requests
from xwtest.common.xwsign import rsaSign
from xwtest.common.param import getRequestNo,getTime
import json
platformNo='6000003612'

class Httpreq():




    def reqBody(self,serviceName,reqData,*userDevice):


        '''封装请求格式'''
        sign=rsaSign(reqData)
        body = {
            "serviceName": serviceName,
            "platformNo": platformNo,
            "userDevice": userDevice,
            "reqData": reqData,
            "keySerial": "1",
            "sign": sign

        }

        return body


    def req_direct(self,serviceName,reqData,*userDevice):
        fixpara={
            'platformNo':platformNo,
            "timestamp":getTime()
        }
        fixpara.update(reqData)

        postdata=self.reqBody(serviceName,json.dumps(fixpara),*userDevice)
        print("请求是",postdata)

        resp=requests.post("http://172.19.60.92:8001/bha-neo-app/lanmaotech/service",data=postdata)
        print("请求结果是",resp.json())
        return resp.json()

dd=Httpreq()




