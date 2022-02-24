import os
import json
import time

def createvpc(CIDR): #vpc 생성
    vpc = os.popen("ncloud vpc createVpc --regionCode KR --vpcName test-vpc --ipv4CidrBlock {}".format(CIDR)).read() 
    data = json.loads(vpc)
    datas = data['createVpcResponse']['vpcList']

    vpcNo = list(d['vpcNo'] for d in datas)
    results = list(map(int, vpcNo))
    global vpcresult
    vpcresult = results[0]    

    print("VPC Number is", vpcresult)
    print("-------------------------------")
    time.sleep(25)
    return getNaclNumber(vpcresult)       #getnaclnumber 함수 조회 시작

def getNaclNumber(a): #nacl 번호조회
    NACL = os.popen("ncloud vpc getNetworkAclList --regionCode KR --vpcNo {}".format(a)).read() 
    NACLdata = json.loads(NACL)
    NACLdatas = NACLdata['getNetworkAclListResponse']['networkAclList']

    NACLNo = list(N['networkAclNo'] for N in NACLdatas)
    NACLresults = list(map(int, NACLNo))
    global NACLresult
    NACLresult = NACLresults[0]
    print("default NACL Number is", NACLresult)
    print("-------------------------------")
    return createsubnet(vpcresult, NACLresult)   #NACL 번호를 반환   

def createsubnet(b, c): #서브넷 생성    
    for x in range(5, 21, 5):           #  서브넷 생성 코드, 유동적이지 못함(수정 필요)
        if x%2 == 1 and x <= 10:
            i = 1
            t = "public"
            os.popen("ncloud vpc createSubnet --regionCode KR --zoneCode KR-{i} --vpcNo {b} --subnetName {t}subnet{i} \
                --subnet 10.0.{x}.0/24 -- networkAclNo {c} --subnetTypeCode {t}".format(i, b, c, x, t)).read()
        elif x%2 == 0 and x <= 10:
            i = 2      
            t = "public"  
            os.popen("ncloud vpc createSubnet --regionCode KR --zoneCode KR-{i} --vpcNo {b} --subnetName {t}subnet{i} \
                --subnet 10.0.{x}.0/24 -- networkAclNo {c} --subnetTypeCode {t}".format(i, b, c, x, t)).read()
        elif x%2 == 1 and x > 10:
            i = 1
            t = "private"
            os.popen("ncloud vpc createSubnet --regionCode KR --zoneCode KR-{i} --vpcNo {b} --subnetName {t}subnet{i} \
                --subnet 10.0.{x}.0/24 -- networkAclNo {c} --subnetTypeCode {t}".format(i, b, c, x, t)).read()
        elif x%2 == 0 and x > 10:
            i = 2
            t = "private"
            os.popen("ncloud vpc createSubnet --regionCode KR --zoneCode KR-{i} --vpcNo {b} --subnetName {t}subnet{i} \
                --subnet 10.0.{x}.0/24 -- networkAclNo {c} --subnetTypeCode {t}".format(i, b, c, x, t)).read()        
    time.sleep(30)
    return getsubnetlist(vpcresult)

def getsubnetlist(vpcno):
    getSUBNET = os.popen("ncloud vpc getSubnetList --regionCode KR --vpcNo {}".format(vpcno)).read()
    datas = getSUBNET["getSubnetListResponse"]["subnetList"]
    subnetNo = list(d['subnetNo'] for d in datas)
    subnetName = list(d['subnetName'] for d in datas)
    subnet = list(d['subnetName'] for d in datas)


CIDR = input("Please Insert VPC-CIDR : ")    #vpc생성 시작 및 CIDR값 입력
print("--------------------------------")
createvpc(CIDR)

