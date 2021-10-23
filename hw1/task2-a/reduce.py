#!/usr/bin/env python

import sys
from collections import defaultdict

table=defaultdict(int)
for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    table[key] = table[key] + 1

print '0,20\t%d' % (table["0,20"])
print '20.01,40\t%d' % (table["20.01,40"])
print '40.01,60\t%d' % (table["40.01,60"])
print '60.01,80\t%d' % (table["60.01,80"])
print '80.01,infinite\t%d' % (table["80.01,infinite"])

