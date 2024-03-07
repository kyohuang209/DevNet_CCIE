from jinja2 import FileSystemLoader, Environment

ports = [
    {
    "type": "Ethernet",
    "slot": 1,
    "number": 1,
    "int_type": "access",
    "vlan": 10
    },
    {
    "type": "Ethernet",
    "slot": 2,
    "number": 2,
    "int_type": "trunk",
    "vlan": 20
    },
    {
    "type": "GigabitEthernet",
    "slot": 3,
    "number": 1,
    "int_type": "trunk",
    "vlan": 30
    }
]

loaders = FileSystemLoader('./')   #定义template所在的文件夹位置

env = Environment(loader=loaders)   # 定义load 模板的环境， 组合上面的一起定义了tempalte所在的环境

template1 = env.get_template('access_trunk.j2')  # 定义template的内容来自某个文件

template1.stream(ports=ports).dump("access_trunk_output.conf")   