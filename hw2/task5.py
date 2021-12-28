from __future__ import print_function
import sys
from csv import reader
from pyspark import SparkContext

if __name__=="__main__":
    sc=SparkContext()
    lines=sc.textFile(sys.argv[1], 1)
    lines=lines.mapPartitions(lambda x: reader(x))
    header=lines.first()
    lines=lines.filter(lambda x: x != header )

    violation=lines.map(lambda x: (x[20], 1))
    violation=violation.reduceByKey(lambda x, y: x+y)
    violation=violation.sortBy(lambda x: x[1], False)

    out=sc.parallelize(violation.take(1))
    output=out.map(lambda x: x[0] + '\t' + str(x[1]))
    output.saveAsTextFile("task5.out")
    sc.stop()
