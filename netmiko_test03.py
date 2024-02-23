# 批量的解析设备

from netmiko import ConnectHandler
from netmiko import SSHDetect
from device_list_info import device_01, device_02
import device_list_info
import re


#define device_info
def get_device_info(ipaddr, username, password):
    device_info = {"device_type":"autodetect",
                    "ip":ipaddr,
                    "username":username,
                    "password":password
                    }
    return device_info

#device type auto detect
def detect_device(device_type):
    print("\n device_type detecting......")
    detect_device = SSHDetect(**device_info)
    device_type = detect_device.autodetect()
    print(f"device type is {device_type}")
    return device_type

#modify device type
def modify_device_type(device_info, device_type):
    device_info["device_type"] = device_type

#ssh connection
def ssh_connect(device_info):
    print("Connect to the Device ......")
    ssh_connect = ConnectHandler(**device_info)

    #ssh_connect.enable()
    
    #send command
    print(f'\n=============show logging===============')
    output = ssh_connect.send_command("show logging")
    #print(output)
    return output

#analyze logging

def analyzer(output):
    match = 0
    pattern = r".*Authentication failed.*"
    result = re.findall(pattern, output)
    for i in result:
        print(i)
        match+=1
    print(f"This 'Authentication failed' issue matched {match} times")



if __name__ == "__main__":
    devicelist = [device_01, device_02]
    for device in devicelist:
        device_info = get_device_info(device["ipaddr"], device["username"], device["password"])
        device_type = detect_device(device_info)
        modify_device_type(device_info, device_type)
        output = ssh_connect(device_info)
        analyzer(output)
    