from ntc_templates.parse import parse_output
import json

if __name__ == "__main__":
    with open("show_version_n9k.log", 'r') as f:
        version_cfg = f.read()
        version_result_parse = parse_output(platform="cisco_nxos", command="show version", data=version_cfg)
        print(json.dumps(version_result_parse, indent=6))

    with open("show_interface_brief_n9k.log", 'r') as e:
        interface_cfg = e.read()
        interface_result_parse = parse_output(platform="cisco_nxos", command="show interface brief", data=interface_cfg)
        print(json.dumps(interface_result_parse, indent=6))
