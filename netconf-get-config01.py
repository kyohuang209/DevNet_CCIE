# Owner: Michael Huang
# Time: 2024/2/15 13:02

from ncclient import manager
from lxml import etree

with manager.connect(host="192.168.1.94",
                     port="830",
                     username="admin",
                     password="cisco123",
                     hostkey_verify=False,
                     device_params={"name":"iosxe"}) as device:

    config  = device.get_config(source="running")
    print(etree.tostring(config.data_ele,pretty_print=True))