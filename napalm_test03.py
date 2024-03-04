from napalm import get_network_driver
import json
import time

os_driver = get_network_driver('nxos_ssh')   #nxos 有两个，需要用ssh这个。 详细参考 https://napalm.readthedocs.io/en/latest/support/index.html#general-support-matrix

with os_driver(hostname="10.124.39.53", username="admin", password="cisco!123") as device:     # 如果是ios， 那么需要加参数optional_args={'secret':'Cisco.123'}
    #print(json.dumps(device.get_facts(), indent='\t'))
    # device.open()
    # print("device is opened")
    device.load_merge_candidate(filename = "napalm_config_test01.cfg")    # 这个地方可以利用config=， 那么就是直接跟命令， 或者用filename= 来跟写好的配置文件
    print(device.compare_config(), '\n', 'before commit')  #比对配置的增删改
    device.commit_config()  #提交配置
    # time.sleep(10)
    print(device.compare_config(), '\n', 'after commit') 
    device.rollback()
    print(device.compare_config(), '\n', 'after rollback') 

    device.close()
    # ip_output = device.get_interfaces_ip()
    # print(json.dumps(ip_output, indent=2))


