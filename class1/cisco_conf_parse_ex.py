#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('/home/jmintz/pynet/pyth_ans_ecourse/class1/cisco_ipsec.txt')

print "EX 8: Printing all crypto map entries with children:\n\n"

crypto_maps = config.find_objects(r'^crypto map')

for map in crypto_maps:
    print map.text
    for child in map.all_children:
        print child.text
    print

print "EX 9: Printing all crypto map entries that use PFS group 2:\n\n"

pfs2_maps = config.find_objects_w_child(parentspec = r'^crypto map', childspec = r"pfs group2")

for map in pfs2_maps:
    print map.text
    for child in map.all_children:
        print child.text
    print

print "EX 10: Printing all crypto map entries that don't use AES:\n\n"

non_aes_maps = config.find_objects_wo_child(parentspec = r'^crypto map', childspec = r'transform-set AES')

for map in non_aes_maps:
    print map.text
    for child in map.all_children:
        print child.text
    print
