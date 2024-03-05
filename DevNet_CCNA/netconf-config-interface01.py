from ncclient import manager
from lxml import etree

device_para = {"host": "192.168.1.94",
               "port": 830,
               "username": "admin",
               "password": "cisco123",
               "hostkey_verify": False,
               "device_params": {"name": "iosxe"}}

device = manager.connect(**device_para)

config_interface_payload = """

        <config>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>GigabitEthernet3</name>
                    <enable>False</enable>
                </interface>
            </interfaces>
        </config>
"""

config = device.edit_config(config_interface_payload, target="running")
print(config)
