import json

para1 = {"level1-01-cisco": {"level2-01-Nexus": {"level3-01-N9K": [9300, 9500], "level3-02-N7K": 7000}, "level2-02-catalyst": "c2960"}, "level1-02-juniper": 'srx'}

para2 = json.dumps(para1, indent=4)
print(para2)
print(type(para2))

para3 = json.loads(para2)
print(para3)
print(type(para3))
