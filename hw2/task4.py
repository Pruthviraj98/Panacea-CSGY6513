from __future__ import print_function
import sys
from pyspark import SparkContext
from csv import reader

if __name__=="__main__":
    sc=SparkContext()
    line=sc.textFile(sys.argv[1], 1)
    line=line.mapPartitions(lambda x: reader(x))
    header=line.first()
    line=line.filter(lambda x:x!=header)

    state_mapper=line.map(lambda x:(("NY" if x[16]=="NY" else "Other"), 1))
    state_reduce=state_mapper.reduceByKey(lambda x, y:x+y)

    output=state_reduce.map(lambda x:x[0]+'\t'+str(x[1]))
    output.saveAsTextFile("task4.out")
    sc.stop()
