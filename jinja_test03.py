from jinja2 import FileSystemLoader, Environment

allowed = ['192.168.1.1', '192.168.2.1', '10.0.0.1']
disallowed = ['192.168.10.254', '192.168.20.254', '10.0.10.254']

loaders = FileSystemLoader('./')   #定义template所在的文件夹位置

env = Environment(loader=loaders)   # 定义load 模板的环境， 组合上面的一起定义了tempalte所在的环境

# device = {"ip": "1.1.1.1", "mask":"255.255.255.0"}

template1 = env.get_template('acl.j2')  # 定义template的内容来自某个文件

# acl.j2里的%前面的横杠是去除空格。 trim_blocks也是去除空格  lstrip_block 也是去除空格  ， 研究下

# result = template1.render(device=device)  # 给模板传参数 并运行模板

template1.stream(allowed=allowed, disallowed=disallowed).dump("acl_output.conf")   



# print(result)