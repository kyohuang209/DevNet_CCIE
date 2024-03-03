from napalm import get_network_driver
import json

ios_driver = get_network_driver('ios')

# ios_driver("192.168.1.84", "admin", "cisco123", optional_args={'port':22})

ios_device01 = ios_driver("192.168.1.84", "admin", "cisco123")

ios_device01.open()

output_arp = ios_device01.get_arp_table()

#print(output_arp)

for arp_info in output_arp:
    print(json.dumps(arp_info, indent=4))


ios_device01.close()