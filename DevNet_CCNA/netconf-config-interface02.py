from ncclient import manager
from lxml import etree

device_para = {"host": "192.168.1.94",
               "port": 830,
               "username": "admin",
               "password": "cisco123",
               "hostkey_verify": False,
               "device_params": {"name": "iosxe"}}

device = manager.connect(**device_para)

config_interface_template = open("netconf-config-interface-template01.xml", "r").read()

config_interface_template.format(int_type="GigabitEthernet",
                                 int_name="3",
                                 int_ip="192.168.1.34",
                                 int_netmask="255.255.255.0")

config = device.edit_config(config_interface_template, target="running")
print(config)
