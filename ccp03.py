from ciscoconfparse import CiscoConfParse

# insert_after 做配置插入

cfg = open("show_run_iosxe.log").read().splitlines()
parse = CiscoConfParse(cfg)

Eth_re = r'interface\s+\w+Ethernet'

for obj in parse.find_objects_wo_child(parentspec=Eth_re, childspec='shutdown'):     #wo 是without的意思， 说这个find_object_wo_child是说在父一级里找没有子一级指定的内容
    obj.insert_after(' shutdown')

for line in parse.ioscfg:
    print(line)
