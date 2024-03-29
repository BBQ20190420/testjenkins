import os
import sys
current_path=os.path.abspath(os.path.dirname(__file__))
rootpath=os.path.split(current_path)[0]
sys.path.append(rootpath)
import unittest
from BeautifulReport import BeautifulReport
import time
from testjenkins.common.sendemail import sendattach

#用例路径
casepath=os.path.join(os.getcwd(),'case')
#报告路径
reportpath=os.path.join(os.getcwd(),'report')


'''
读取用例
'''

def addcase():
    discover=unittest.defaultTestLoader.discover(casepath,pattern='test*.py',top_level_dir=None)
    return discover

'''
执行用例
'''

def run(case):
    result=BeautifulReport(case)
    formattime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    formatreport=f"report{formattime}.html"
    result.report(description="倩倩测试",report_dir=reportpath,filename=formatreport)
    emailpath=os.path.join(reportpath,formatreport)
    sendattach(emailpath)


if __name__ == '__main__':
    cases=addcase()
    for i in cases:
        run(i)

