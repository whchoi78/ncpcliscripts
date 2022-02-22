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
    return vpcresult       #vpc 번호를 반환

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
    return NACLresult   #NACL 번호를 반환



CIDR = input("Please Insert CIDR : ")    #CIDR값 입력

createvpc(CIDR)
getNaclNumber(vpcresult)