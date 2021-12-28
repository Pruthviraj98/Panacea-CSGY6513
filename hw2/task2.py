from __future__ import print_function
import sys
from csv import reader
from pyspark import SparkContext

if __name__ == "__main__":

    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x))

    header = lines.first()
    data = lines.filter(lambda x: x != header )

#violation = lines.map(lambda x: (x[7], 1)).reduceByKey(lambda x, y: x + y)
#output = violation.map(lambda x: x[0] + '\t' + str(x[1]))

    violation = data.map(lambda x: (x[7], 1 ))
    violations_reduced  = violation.reduceByKey(lambda x, y: x + y)
    output = violations_reduced.map(lambda x: x[0] + '\t' + str(x[1])).sortBy(lambda x: x[0], True) 

    output.saveAsTextFile("task2.out")

    sc.stop()
