from lxml import etree

device_para = {"host":"192.168.1.94",
               "port":830,
               "username":"admin",
               "password":"cisco123",
               "hostkey_verify":False,
               "device_params":{"name":"iosxe"}}

device = manager.connect(**device_para)
config = device.get_config(source="running")
print(etree.tostring(config.data_ele,pretty_print=True))