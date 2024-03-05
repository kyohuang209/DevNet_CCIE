from lxml import etree

device_para = {"host":"192.168.1.94",
               "port":830,
               "username":"admin",
               "password":"cisco123",
               "hostkey_verify":False,
               "device_params":{"name":"iosxe"}}

device = manager.connect(**device_para)

get_interface_payload =

        <filter>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>GigabitEthernet3</name>
                </interface>
            </interfaces>
        </filter>

config = device.get((get_interface_payload))
print(etree.tostring(config.data_ele,pretty_print=True))