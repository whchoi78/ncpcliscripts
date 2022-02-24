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
    time.sleep(20)
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
    global SUBNET    
    for x in range(5, 21, 5):           #  서브넷 생성 코드, 유동적이지 못함(수정 필요)
        if x%2 == 1 and x <= 10:
            i = "1"
            T = "PUBLIC"
            SUBNET = os.popen("ncloud vpc createSubnet --regionCode KR --zoneCode KR-{0} --vpcNo {1} --subnetName {5}subnet{0} \
                --subnet 10.0.{3}.0/24 --networkAclNo {2} --subnetTypeCode {4}".format(i, b, c, x, T, t)).read()
        elif x%2 == 0 and x <= 10:
            i = "2"      
            T = "PUBLIC"  
            t = T.lower()
            SUBNET = os.popen("ncloud vpc createSubnet --regionCode KR --zoneCode KR-{0} --vpcNo {1} --subnetName {5}subnet{0} \
                --subnet 10.0.{3}.0/24 --networkAclNo {2} --subnetTypeCode {4}".format(i, b, c, x, T, t)).read()
        elif x%2 == 1 and x > 10:
            i = "1"
            T = "PRIVATE"
            t = T.lower()
            SUBNET = os.popen("ncloud vpc createSubnet --regionCode KR --zoneCode KR-{0} --vpcNo {1} --subnetName {5}subnet{0} \
                --subnet 10.0.{3}.0/24 --networkAclNo {2} --subnetTypeCode {4}".format(i, b, c, x, T,t)).read()
        elif x%2 == 0 and x > 10:
            i = "2"
            T = "PRIVATE"
            t = T.lower()
            SUBNET = os.popen("ncloud vpc createSubnet --regionCode KR --zoneCode KR-{0} --vpcNo {1} --subnetName {5}subnet{0} \
                --subnet 10.0.{3}.0/24 --networkAclNo {2} --subnetTypeCode {4}".format(i, b, c, x, T, t)).read()        
    time.sleep(25)
    return getsubnetlist(vpcresult)

def getsubnetlist(vpcno):
    getSUBNET = os.popen("ncloud vpc getSubnetList --regionCode KR --vpcNo {}".format(vpcno)).read()
    datas = getSUBNET["getSubnetListResponse"]["subnetList"]
    subnetNo = list(d['subnetNo'] for d in datas)
    subnetName = list(d['subnetName'] for d in datas)
    subnet = list(d['subnetName'] for d in datas)
    for a in subnetNo:
        print("subnet number is {}".format(a))
    for a in subnetName:
        print("subnet name is {}".format(a))
    for a in subnet:
        print("subnet CIDR is {}".format(a))


CIDR = input("Please Insert VPC-CIDR : ")    #vpc생성 시작 및 CIDR값 입력
print("--------------------------------")
createvpc(CIDR)

