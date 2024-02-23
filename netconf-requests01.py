# Owner: Michael Huang
# Time: 2024/2/16 16:02
import json
import requests

from requests.auth import HTTPBasicAuth

auth_info = HTTPBasicAuth("admin", "cisco123")
header_info = {"Accept": "application/yang-data+json"}
url = "https://developer-cisco.cn:8130/.well-known/host-meta"

response = requests.get(url, headers=header_info, auth=auth_info, verify=False)
print(response)

print(response.text)