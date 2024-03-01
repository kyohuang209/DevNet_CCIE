# import library
import textfsm

# open the tempalte file
with open('cisco_ios_show_ip_int_brief.textfsm', 'r') as f:
    template = textfsm.TextFSM(f)

# define the show output to be parsed
output_info = '''
show ip int brief
Interface           IP-Address      OK? Method  Status                  Protocol
GigabitEthernet1    192.168.1.94    YES NVRAM   up                      up
GigabitEthernet2    unassigned      YES NVRAM   administratively down   up
GigabitEthernet3    101.1.1.5       YES other   administratively down   up
GigabitEthernet4    2.1.1.1         YES other   up                      up
GigabitEthernet5    unassigned      YES NVRAM   up                      up
Loopback0           1.1.1.1         YES manual  up                      up
Tunnel100           100.1.1.1       YES manual  up                      up
'''

interfaces = template.ParseText(output_info)
print(interfaces)
print(type(interfaces))

for i in interfaces:
    print(i)