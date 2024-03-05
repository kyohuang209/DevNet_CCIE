from netmiko import ConnectHandler
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import NetmikoTimeoutException

# set device info

cisco_device01 = {"device_type": "cisco_ios",
                  "ip": "192.168.1.84",
                  "username": "admin",
                  "password": "cisco123",
                  "secret": "cisco123"}

# netmiko ssh connect
print(f'\n=============Connect To Device {cisco_device01["ip"]}===============')
shi_connect = ConnectHandler(**cisco_device01)

# netmiko enable
shi_connect.enable()

# send command
print(f'\n=============show ip configuration of Device {cisco_device01["ip"]}==================')
output = shi_connect.send_command("show ip int brief")
print(output)

# send config
print(f'\n=============send config of Device {cisco_device01["ip"]}==================')
config_list = ["interface loopback 10", "ip address 10.10.10.10 255.255.255.255"]
config_01 = shi_connect.send_config_set(config_list)
print(config_01)