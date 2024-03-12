from jinja2 import FileSystemLoader, Environment
import yaml


loaders = FileSystemLoader('./')   #定义template所在的文件夹位置

env = Environment(loader=loaders)   # 定义load 模板的环境， 组合上面的一起定义了tempalte所在的环境
test = Environment()
template1 = env.get_template('bgp.j2')  # 定义template的内容来自某个文件

host = ["bgp_param01", "bgp_param02"]

for i in host:
    config_list = yaml.safe_load(open(f"./{i}.yml"))

# print(type(config_list))

    output = template1.stream(config_list).dump(f"./bgp_output_{i}.conf")