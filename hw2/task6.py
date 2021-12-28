from __future__ import print_function
import sys
from csv import reader
from pyspark import SparkContext
from decimal import Decimal

if __name__=="__main__":
    sc=SparkContext()
    lines=sc.textFile(sys.argv[1], 1)
    lines=lines.mapPartitions(lambda x: reader(x))
    header=lines.first()
    lines=lines.filter(lambda x: x != header)

    violation_mapper=lines.map(lambda x: (x[20], 1))
    violation_reducer=violation_mapper.reduceByKey(lambda x, y: x+y).sortBy(lambda x: [-x[1], x[0]])
    firstOut=sc.parallelize(violation_reducer.take(10))
    output=firstOut.map(lambda x: x[0]+'\t'+str(x[1]))
    output.saveAsTextFile("task6.out")
    sc.stop()
