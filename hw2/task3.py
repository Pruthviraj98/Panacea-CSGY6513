from __future__ import print_function
import sys
from csv import reader
from pyspark import SparkContext

if __name__=="__main__":
    sc=SparkContext()
    lines=sc.textFile(sys.argv[1], 1)
    lines=lines.mapPartitions(lambda x: reader(x))
    header=lines.first() 
    lines=lines.filter(lambda x: x != header)
    
    amount=lines.map(lambda x:(x[5], float(x[12])))
    total=amount.reduceByKey(lambda x, y:x+y)

    precintType=lines.map(lambda x:(x[5], 1))
    precintDistribution=precintType.reduceByKey(lambda x, y: x+y)

    totalavg=total.join(precintDistribution)
    outtotalavg=totalavg.map(lambda x: "%s\t%.2f, %.2f" % (x[0], x[1][0], x[1][0]/x[1][1])).sortByKey()
    outtotalavg.saveAsTextFile("task3.out")
    sc.stop()
