from jinja2 import FileSystemLoader, Environment
import yaml


loaders = FileSystemLoader('./')   #定义template所在的文件夹位置

env = Environment(loader=loaders)   # 定义load 模板的环境， 组合上面的一起定义了tempalte所在的环境

template1 = env.get_template('bgp.j2')  # 定义template的内容来自某个文件

# template1.stream(ASN = 65001, 
#                  neighbor = "172.16.1.1",
#                  peer_ASN = 65002, 
#                  network_int = "172.16.1.0",
#                  mask_int = "255.255.255.0",
#                  network_ext = "192.168.1.0",
#                  mask_ext = "255.255.255.0",
#                  protocol = "ospf",
#                  process_id = "100"         
#                  ).dump("bgp_output.conf")   

config_list = yaml.safe_load(open("./bgp_param01.yml"))

# print(type(config_list))

output = template1.stream(config_list).dump("./bgp_output2.conf")