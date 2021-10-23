#!/usr/bin/env python

from operator import itemgetter
import sys
from datetime import datetime as dt
from csv import reader

curr_trips = []
curr_fares = []
curr_key = None
for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = value.strip().split(',')
    if curr_key == None:
        curr_key = key
    # buffer the value
    if curr_key == key:
        if len(value)>7:
            curr_trips=value
        else:
            curr_fares=value

    # We've read all the lines which have the same key, do many-to-many join and update to buffer new lines
    else:
        if curr_key != None:
	    if len(curr_fares)!=0 and len(curr_trips)!=0:
      	        print '%s\t%s,%s'%(curr_key,','.join(curr_trips),','.join(curr_fares))

        # update key
        curr_key = key
        # clean buffer
        curr_trips = []
        curr_fares = []
        # buffer the value
        if len(value)>7:
            curr_trips=value
        else:
            curr_fares=value

if curr_key == key:
    if len(curr_fares)!=0 and len(curr_trips)!=0:
        print '%s\t%s,%s'%(curr_key,','.join(curr_trips),','.join(curr_fares))
