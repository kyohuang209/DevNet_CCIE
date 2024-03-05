import xml.etree.ElementTree as XEET

devnet_tree = XEET.parse("interfaces.xml")  #加载xml
root = devnet_tree.getroot()
print(root.attrib)

interfaces = root.findall("./*/interface/name") #指定路径方式搜索

for interface in interfaces:
    print(interface.text)
    print(interface)