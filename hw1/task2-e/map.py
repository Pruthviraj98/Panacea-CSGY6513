#!/usr/bin/env python

import sys
import os
import string

for line in sys.stdin:
    key, val=line.strip().split("\t", 1)
    key=key.strip().split(",")
    print "%s\t%d"%(key[0], 1)
	

