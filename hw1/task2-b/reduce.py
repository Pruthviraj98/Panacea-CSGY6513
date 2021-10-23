#!/usr/bin/env python

import sys

current_sum=0

for line in sys.stdin: 
    try:
        key, val = line.strip().split('\t', 1)
	val=int(val)
	current_sum+=val
    except ValueError:
	continue

print "%d"%(current_sum)
