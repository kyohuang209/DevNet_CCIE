from ciscoconfparse import CiscoConfParse

parse01 = CiscoConfParse(config="show_run_iosxe.log", syntax='ios', factory=True)

for int_obj in parse01.find_objects(linespec='^interface'):
    # print("Interface with shutdown command: ", int_obj.text)
    int_name = int_obj.re_match_typed("^interface\s+(\S.+)")    # re_match_typed  匹配父规范
    int_add = int_obj.re_match_iter_typed("ip\saddress\s(\d+\.\d+\.\d+\.\d+)\s", result_type = str)  #re_match_iter_typed 匹配子规则
    print(f"{int_name} has ip address {int_add}")
    