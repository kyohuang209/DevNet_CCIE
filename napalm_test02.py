from napalm import get_network_driver
import json

ios_driver = get_network_driver('ios')

# ios_driver("192.168.1.84", "admin", "cisco123", optional_args={'port':22})

# ios_device01 = ios_driver("192.168.1.84", "admin", "cisco123")

# ios_device01.open()

# output_facts = ios_device01.get_facts()

# #print(output_facts)

# for arp_info in output_arp:
#     print(json.dumps(arp_info, indent=4))

# print(output_facts)
# print(json.dumps(output_facts, indent='t'))

# ios_device01.close()

with ios_driver("192.168.1.84", "admin", "cisco123") as device:
    print(json.dumps(device.get_facts(), indent='\t'))