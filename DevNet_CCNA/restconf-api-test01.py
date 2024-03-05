import requests
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

auth_info =HTTPBasicAuth("admin","cisco123")
headers_info = {"Accept":"application/yang-data+json"}
url = "https://developer-cisco.cn:10831/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=4"

if __name__ == "__main__":
    response= requests.get(url, headers=headers_info, auth = auth_info, verify = False)
    print(response)
    print(response.text)