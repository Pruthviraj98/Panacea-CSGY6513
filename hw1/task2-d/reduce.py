#!/usr/bin/env python

import sys

diction={}
for line in sys.stdin:
    key, val=line.strip().split("\t")
    revenue_amount, tip_amount=val.split(",")
    if key not in diction:
	diction[key]=[float(revenue_amount), float(tip_amount)]
    else:
	diction[key][0]+=float(revenue_amount)
	diction[key][1]+=float(tip_amount)

keys=list(diction.keys())
values=list(diction.values())

for i in range(len(keys)):
    print (keys[i]+"\t"+"{:.2f}".format(values[i][0])+","+"{:.2f}".format(values[i][1]))
