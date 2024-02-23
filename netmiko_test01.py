from netmiko import ConnectHandler
from netmiko.cisco import CiscoIosTelnet
from netmiko import SSHDetect



#define device_info
device01_info = {"device_type":"autodetect",
                 "ip":"10.124.39.53",
                 "username":"admin",
                 "password":"cisco!123"
                }

#device type auto detect
print("\n device_type detecting......")
detect_device = SSHDetect(**device01_info)
device01_type = detect_device.autodetect()
print(f"device01 type is {device01_type}")


#ssh connection
print("Connect to the Device ......")
ssh_connect = ConnectHandler(**device01_info)


#send command
print(f'\n=============show ip int brief===============')
output = ssh_connect.send_command("show ip int brief")
print(output)