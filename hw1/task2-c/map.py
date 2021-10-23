#!/usr/bin/env python

import sys
import os

for line in sys.stdin:
   key, val=line.strip().split("\t", 1)
   val=val.strip().split(",")
   print "%s\t%d"%(val[3], 1)
