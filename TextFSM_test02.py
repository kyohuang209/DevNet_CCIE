from netmiko import ConnectHandler
import time
import json

device_info = {"device_type":"cisco_nxos",
                "ip":"10.124.39.53",
                "username": "admin",
                "password": "cisco!123"
                }

connect = ConnectHandler(**device_info)

interfaces = connect.send_command("show ip int brief", use_textfsm=True)
time.sleep(3)

for interface in interfaces:
    print(json.dumps(interface,indent="\t"))
