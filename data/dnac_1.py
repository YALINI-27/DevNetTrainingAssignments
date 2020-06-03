import requests
import json

def get_data(username,password):
    url = 'https://sandboxdnac2.cisco.com/api/system/v1/auth/token'

    payload = {}
    headers = {
        'Authorization': 'Basic ZG5hY2RldjpEM3Y5M1RAd0sh'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    res = json.loads(response.text.encode('utf8'))

    token = res["Token"]

    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'

    payload = {}
    headers = {
        'x-auth-token': token
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    res1 = json.loads(response.text.encode('utf8'))

    return(res1)

if __name__ =='__main__':
    print('  Device Details  ')
    print('-------------------')
    username = input("Enter username : ")
    password = input("Enter password : ")
    device_data=get_data(username,password)
    for dnac_devices in device_data['response']:
            print('\nDevice ID :', dnac_devices['id'])
            print('Device Type :', dnac_devices['type'])
            print('Device Family :', dnac_devices['family'])
            print('Software Type :', dnac_devices['softwareType'])
            print('Management IP Address :', dnac_devices['managementIpAddress'],'\n')