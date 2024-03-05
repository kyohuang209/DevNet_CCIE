import requests
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

auth_info =HTTPBasicAuth("admin","cisco123")
headers_info = {"Accept":"application/yang-data+json"}
url = "https://developer-cisco.cn:10831/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=4"

data01 = {"Cisco-IOS-XE-native:primary": {"address": "20.1.1.1", "mask": "255.0.0.0"}}
parameter = json.dumps(data01)


if __name__ == "__main__":
    response1= requests.patch(url, headers=headers_info, auth = auth_info, verify = False, data = parameter)
    print("HTTP Status Code:", response1.status_code)
    print(response1.text)

    response= requests.get(url, headers=headers_info, auth = auth_info, verify = False)
    print(response)
    print(response.text)