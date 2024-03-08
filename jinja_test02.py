from jinja2 import FileSystemLoader, Environment

loaders = FileSystemLoader('./')   #定义template所在的文件夹位置

env = Environment(loader=loaders)   # 定义load 模板的环境， 组合上面的一起定义了tempalte所在的环境

device = {"ip": "1.1.1.1", "mask":"255.255.255.0"}

template1 = env.get_template('first.j2')  # 定义template的内容来自某个文件

result = template1.render(device=device)  # 给模板传参数 并运行模板

print(result)