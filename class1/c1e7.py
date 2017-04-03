#!/usr/bin/env python

from pprint import pprint as pp
import json, yaml

print "Opening YAML file:\n\n"
with open('c1.yml','r') as yml:
    pp(yaml.load(yml))

print "\n\nOpening JSON file:\n\n"
with open('c1.json','r') as jsn:
    pp(json.load(jsn))
