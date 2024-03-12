import requests
import json

requests.packages.urllib3.disable_warnings()   # 去掉warning message 

def Get_Token():
    url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

    payload = """
    {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"
        }
    }
    }
    """
    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'APIC-cookie=eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc1OGp1ZjV5aWgyZWgzdDBxcjZrcHQ0ZXpuM2trMWRjIiwidHlwIjoiand0In0.eyJyYmFjIjpbeyJkb21haW4iOiJhbGwiLCJyb2xlc1IiOjAsInJvbGVzVyI6MX1dLCJpc3MiOiJBQ0kgQVBJQyIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyaWQiOjE1Mzc0LCJ1c2VyZmxhZ3MiOjAsImlhdCI6MTcxMDI0MjUyMywiZXhwIjoxNzEwMjQzMTIzLCJzZXNzaW9uaWQiOiI0a2RHVktmb1JIU3J5K3g3ckxmL3FBPT0ifQ.mkFXyGkwcIJ-Yg9DkhuRCXu_sCLpLSdgSNaerTV9Jz5D3EyUzZcZ08DJy1Jm3mEWErARMXFdKbCFkpcNgtoROihbwaEBljLYEjN-jFpmXtmAMYbYpW6vEfX7clG9edFtZ_06w-hLgJOaz5zgf_v95oFpBo5AsDhAGPdT9vjofAFtIBHZfdi3060B1Xf7An8E61Xrhxp_PWHCaCWH79wDmWtDxQv5fLF-kdFJG2nWPILXtiA0TutBegXfBkQDtmK7KN18DzzAw71XpmhM0_l_LmBqEUqJa763z6oAIg1BT_EBJe-X0UcUfTsa6zgCXAy6xeals0GWcvloXYtQQGNiWA'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    token_info = response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]

    return token_info



def Get_Tenant(token_info):
    url = "https://sandboxapicdc.cisco.com/api/class/fvTenant.json"

    payload = {}
    headers = {
    # 'token': {token_info},
    'Cookie': f'APIC-cookie={token_info}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(json.dumps(response.json(), indent='\t'))



def Post_Tenent(token_info, Tenent_name):

    url = "https://sandboxapicdc.cisco.com/api/mo/uni.json"

    payload = json.dumps({
    "fvTenant": {
        "attributes": {
        "dn": f"uni/tn-{Tenent_name}",
        "rn": f"{Tenent_name}",
        "name": f"{Tenent_name}",
        "status": "created"
        }
    }
    })
    headers = {
    # 'token': f'{token_info}',
    'Content-Type': 'application/json',
    'Cookie': f'APIC-cookie={token_info}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print(response.text)

token_info1 = Get_Token()

# print("token is ", token_info1)
Get_Tenant(token_info1)
Post_Tenent(token_info1, "mk-test002")