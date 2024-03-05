from xml.dom.minidom import parse   #导入模块

devnet_domTree = parse("interfaces.xml")  #加载xml文件
collection = devnet_domTree.documentElement  #读取根元素信息

if collection.hasAttribute("vendor"):
    print(collection.getAttribute("vendor"))

interfaces = collection.getElementsByTagName("interface")  #基于XML标签名称“interface”获取过滤信息

for interface in interfaces:
    print(interface.getElementsByTagName("name")[0].firstChild.data)