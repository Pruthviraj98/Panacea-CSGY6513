from __future__ import print_function
import sys
from pyspark import SparkContext
from csv import reader
if __name__ == "__main__":
    sc = SparkContext.getOrCreate()
    line1 = sc.textFile(sys.argv[1], 1)
    line2 = sc.textFile(sys.argv[2], 1)
    open_data = line2.mapPartitions(lambda x: reader(x))
    parking_data = line1.mapPartitions(lambda x: reader(x))
    
    open_mapper = open_data.map(lambda x:(x[0],""))
    park_mapper = parking_data.map(lambda x:(x[0],x[3]+", "+x[16]+", "+x[2]+", "+x[1]))
    
    output=park_mapper.leftOuterJoin(open_mapper).filter(lambda x:x[1][1]==None).sortByKey()
    output=output.map(lambda x: x[0]+"\t"+x[1][0])
    output.saveAsTextFile("task1.out")
    sc.stop()
