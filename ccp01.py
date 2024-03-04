from ciscoconfparse import CiscoConfParse

parse01 = CiscoConfParse(config="show_run_iosxe.log", syntax='ios', factory=True)

for int_obj in parse01.find_objects_w_child(parentspec='^interface',childspec="^\s+shutdown"):
    print("Interface with shutdown command: ", int_obj.text)
