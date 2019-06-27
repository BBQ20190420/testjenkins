import unittest
import os
from BeautifulReport import BeautifulReport
import time

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

if __name__ == '__main__':
    cases=addcase()
    for i in cases:
        run(i)

