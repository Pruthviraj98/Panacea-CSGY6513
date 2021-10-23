#!/usr/bin/env python

import sys
import os

diction={}
for line in sys.stdin:
    key, val=line.strip().split("\t")
    if key not in diction:
	diction[key]=1
    else:
	diction[key]+=1

vals=list(diction.values())
keys=list(diction.keys())
for i in range(len(vals)):
    print "%s\t%d"%(keys[i], vals[i])
