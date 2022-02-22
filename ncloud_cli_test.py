import os
import json

region = os.popen("ncloud server getRegionList").read()
data = json.loads(region)
datas = data['getRegionListResponse']['regionList']

print(list(d['regionName'] for d in datas))
