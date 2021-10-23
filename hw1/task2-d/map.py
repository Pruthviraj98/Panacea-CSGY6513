#!/usr/bin/env python

import sys
import os
import string
from datetime import datetime

for line in sys.stdin:
    key, val=line.strip().split("\t", 1)
    vals=val.strip().split(",")
    
    amount=float(vals[11])+float(vals[12])+float(vals[14])
    pickUpDate=key.strip().split(",")[3]
    temp=pickUpDate[0:10]
    print '%s\t%f,%f'%(temp, amount, float(vals[14]))
