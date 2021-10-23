#!/usr/bin/env python

import sys
import os
import string

for line in sys.stdin: 
    key, value = line.strip().split('\t', 1)
    fare_price = float(value.strip().split(',')[11])
    if(fare_price > 0 and fare_price <=20):
      	print '0,20\t%f' % (fare_price)
    elif (fare_price > 20.00 and fare_price <= 40):
        print '20.01,40\t%f' % (fare_price)     
    elif (fare_price > 40.00 and fare_price <= 60):
        print '40.01,60\t%f' % (fare_price)
    elif (fare_price > 60.00 and fare_price <= 80):
        print '60.01,80\t%f' % (fare_price)
    elif (fare_price > 80.00):
        print '80.01,infinite\t%f' % (fare_price)
