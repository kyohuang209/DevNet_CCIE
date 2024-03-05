import re

pattern = "\[BDrip\]"

s = "hello[BDrip]world"

result = re.findall(pattern, s)

print(result)

#print(result.group())