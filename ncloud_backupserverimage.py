#! /usr/bin/python3
from datetime import datetime
import os
import json
import time

def createserverimage():                        #서버 이미지 생성 함수
    day = datetime.today().strftime("%Y%m%d")
    create = os.popen("ncloud server createMemberServerImage --serverInstanceNo 10431198 --memberServerImageName test-{}".format(day)).read()
    # 8번 줄 현재 날짜 기준으로 서버 이미지 생성
    time.sleep(120)

    return getserverlists()                     #서버 이미지 조회 반환


def getserverlists():                           #서버 이미지 조회 함수 및 조회 된 값 리스트 선언
    show = os.popen("ncloud server getMemberServerImageList").read()        #서버 이미지 조회
    data = json.loads(show)
    #서버 이미지를 조회하면은 json형식으로 출력 되기 때문에 필요한 값 추출
    datasNo = data['getMemberServerImageListResponse']['memberServerImageList']     
    ImageNo = list(d['memberServerImageNo'] for d in datasNo)
    global resultNo
    resultNo = list(map(int, ImageNo))

    return deleteserverimage()              #서버 이미지 삭제 함수 반환

def deleteserverimage():                    #서버 이미지 삭제 함수
    DelresultNo = resultNo[1]    # 이전 생성 된 서버 이미지 값 추출
    rm = os.popen("ncloud server deleteMemberServerImages --memberServerImageNoList {}".format(DelresultNo)).read()
    # 이전 생성 된 서버 이미지 삭제

createserverimage()         # 서버 이미지 생성 시작