from napalm import get_network_driver
import json

ios_driver = get_network_driver('ios')

with ios_driver("10.124.39.53", "admin", "cisco!123") as device:
    #print(json.dumps(device.get_facts(), indent='\t'))
    device.load_merge_candidate(file = "napalm_config_test01.cfg")  