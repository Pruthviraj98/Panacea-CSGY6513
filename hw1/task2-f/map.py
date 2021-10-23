#!/usr/bin/env python

import sys
import os
import string

for line in sys.stdin:
    key, val=line.strip().split("\t", 1)
    keys=key.strip().split(",")
    medallion=keys[0]
    h_license=keys[1]
    print "%s\t%s"%(h_license, medallion)
