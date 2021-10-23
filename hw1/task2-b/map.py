#!/usr/bin/env python

import sys

for line in sys.stdin: 
    key, value = line.strip().split('\t')
    value = value.strip().split(',')
    try:
        total_amount=float(value[-1])
    except ValueError:
	continue

    if total_amount<=15:
        print "%s\t%d"%("0,15", 1)
