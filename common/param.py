import time
import uuid


def getTime():
    formattime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    return formattime

def getRequestNo():
    requestNo="".join(str(uuid.uuid4()).split("-"))
    return requestNo


