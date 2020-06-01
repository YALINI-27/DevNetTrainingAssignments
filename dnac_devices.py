import json

#opening dnac_devices.json file
with open("dnac_devices.json",'r') as data:
    json_data = json.load(data)

#displaying data
for item in json_data["response"]:
    print(item["id"])
    print(item["type"])
    print(item["family"])
    print(item["softwareType"])
    print(item["managementIpAddress"])
    # print()