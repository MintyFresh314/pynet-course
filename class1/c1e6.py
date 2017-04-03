#!/usr/bin/env python

import yaml, json

test_list = range(10)

dog = { 'name' : 'Spot', 'breed' : 'Golden Retreiver', 'weight' : 75 }

test_list.append(dog)

with open('c1.yml', 'w') as yaml_file:
    yaml_file.write(yaml.dump(test_list, default_flow_style = False))

with open('c1.json', 'w') as json_file:
    json.dump(test_list, json_file)

