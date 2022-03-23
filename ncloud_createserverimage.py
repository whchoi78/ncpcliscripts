from datetime import datetime
import os
import json
import time

def createserverimage():
    day = datetime.today().strftime("%Y%m%d")
    create = os.popen("ncloud server createMemberServerImage --serverInstanceNo 10412252 --memberServerImageName test-{}".format(day)).read()
    time.sleep(150)
    return getserverlists()


def getserverlists():
    show = os.popen("ncloud server getMemberServerImageList").read()
    data = json.loads(show)
    
    datasNo = data['getMemberServerImageListResponse']['memberServerImageList']
    ImageNo = list(d['memberServerImageNo'] for d in datasNo)
    resultNo = list(map(int, ImageNo))

    datasName = data['getMemberServerImageListResponse']['memberServerImageList']
    ImageName = list(d['memberServerImageName'] for d in datasName)
    resultName = list(map(str, ImageName))

    global Imagedict
    Imagedict = dict(zip(resultName, resultNo))