import yaml
import json

with open("yaml_s2.json", "r") as file:
    json_file01 = file.read()
    print(json_file01)

    # yaml_data01 = yaml.dump(json_file01)
    # print(yaml_data01)

    yaml_data01 = yaml.full_load(json_file01)
    print(yaml_data01)

    yaml_data02 = yaml.dump(yaml_data01)
    print(yaml_data02)