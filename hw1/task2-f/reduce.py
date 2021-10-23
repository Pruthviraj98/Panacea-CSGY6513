#!/usr/bin/env python

import sys
import os
from collections import defaultdict

diction=defaultdict(set)
for line in sys.stdin:
    key, val=line.strip().split("\t", 1)
    diction[key].add(val)    


for keys, vals in diction.items():
    print(keys+"\t"+str(len(vals)))
