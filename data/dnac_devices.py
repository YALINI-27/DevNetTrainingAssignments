import json

#opening dnac_devices.json file
with open("dnac_devices.json",'r') as data:
    json_data = json.load(data)

#displaying data
for item in json_data["response"]:
    print(' ID :', item["id"])
    print('Type :',item["type"])
    print('Family :',item["family"])
    print('Software Type :',item["softwareType"])
    print('Management IP Address :',item["managementIpAddress"])
    