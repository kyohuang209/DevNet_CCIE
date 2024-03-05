import json


para0 = {"b": "Nexus", "c": "cisco", "a": "15.5"}

"""
print(para1)
print(type(para1))

para2 = json.dumps(para1)
para2 = json.dumps(para1,sort_keys=True)

print(para2)
print(type(para2))

"""

para1 = json.dumps(para0)
para2 = json.dumps(para0, indent=4)
para3 = json.dumps(para0, indent=4, separators=(",", ":"))

print(len(para1))
print(para1)
print(len(para2))
print(para2)
print(len(para3))
print(para3)
