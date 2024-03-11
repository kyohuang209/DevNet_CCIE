import yaml
import json

with open("yaml_s1.yaml", "r") as file:
    yaml_file01 = file.read()
    yaml_data01 = yaml.full_load(yaml_file01)
    print(json.dumps(yaml_data01, indent="\t"))