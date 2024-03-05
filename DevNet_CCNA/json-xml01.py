import xmltodict
import json

data1 = '{"vendor":"cisco","N9K-Type":[9300,9500]}'
data1 = json.loads(data1)
data1 = {"root":data1}

xmldata01 = xmltodict.unparse(data1,pretty=True)
print(xmldata01)

with open("test-dict-xml.xml","w") as f:
    f.write(xmldata01)
