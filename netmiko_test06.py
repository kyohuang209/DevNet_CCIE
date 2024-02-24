# 批量的解析设备, 并处理异常中断的处理

from netmiko import ConnectHandler
from netmiko import SSHDetect
from netmiko import NetmikoTimeoutException
from netmiko import NetmikoAuthenticationException
from netmiko.exceptions import NetmikoBaseException
#from device_list_info import device_01, device_02, device_03
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
    print('\n',f'Start connecting to device {device_info["ip"]} ......' )
    try:
        print("\n Device_type detecting......")
        detect_device = SSHDetect(**device_info)
        device_type = detect_device.autodetect()
    except NetmikoTimeoutException:
        print('\n', '*'*30, f'Task: {device_info["ip"]} Network Connection failure', '*'*30, "\n")
        return "error"
    except NetmikoAuthenticationException:
        print("\n", "*"*30, f'Task: {device_info["ip"]} Authentication failure', "*"*30,"\n" )
        return "error"
    except NetmikoBaseException:
         print("\n", "*"*30, f'Task: {device_info["ip"]} Base Error', "*"*30, "\n" )       
    else:
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
    print(f'\n','='*30,'show logging','='*30)
    output = ssh_connect.send_command("show logging")
    #print(output)
    return output

#analyze logging

def analyzer(output, device_info):
    match = 0
    pattern = r".*Authentication failed.*"
    result = re.findall(pattern, output)
    print('='*30,f'Device {device_info["ip"]} is under analyzing','='*30,'\n')
    for i in result:
        print(i)
        match+=1
    print('='*30,f'Device {device_info["ip"]} analysis done','='*30,'\n')
    print(f"This 'Authentication failed' issue matched {match} times",'\n')


if __name__ == "__main__":

    with open("device_info01.txt", "r") as f:
        str1 = f.read()
        print(str1)
        devices = str1.split("\n")
        #print(devices)
        #print(type(devices))
        for device in devices:
            device = device.split(" ")
            #print(device)
            #print(type(device))
    
            #devicelist = [device_01, device_02, device_03]
            #for device in devicelist:
            device_info = get_device_info(device[0], device[1], device[2])
            device_type = detect_device(device_info)
            if device_type != "error":
                modify_device_type(device_info, device_type)
                output = ssh_connect(device_info)
                analyzer(output,device_info)
    
