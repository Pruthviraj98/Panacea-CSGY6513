#!/usr/bin/env python

import sys
import os

diction={}

for line in sys.stdin:
    key, val=line.strip().split("\t", 1)
    if key not in diction:
	diction[key]=1
    else:
	diction[key]+=1
    
vals=list(diction.values())
avgs=[]
for i in vals:
    avgs.append(i//6)

keys=list(diction.keys())

for i in range(len(keys)):
    print "%s\t%d,%d"%(keys[i], vals[i], avgs[i])

