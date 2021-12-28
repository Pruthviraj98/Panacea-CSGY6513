from __future__ import print_function
from pyspark import SparkContext
import sys
from csv import reader

if __name__=="__main__":
    sc=SparkContext()
    lines=sc.textFile(sys.argv[1], 1)
    lines=lines.mapPartitions(lambda x: reader(x))
    header=lines.first() 
    lines=lines.filter(lambda x:x!=header)

    days=lines.map(lambda x: (x[3], x[1])).sortByKey()
    days=days.groupByKey().map(lambda x :(x[0],list(x[1])))

    def daysParser(temp):
        (weekday, weekend)=(0, 0)
        for i in range (0,len(temp)):
            if temp[i] in ['2016-03-05','2016-03-06','2016-03-12','2016-03-13','2016-03-19','2016-03-20','2016-03-26','2016-03-27']:
                weekend+=1
            else:
                weekday+=1
        weekday=float(weekday/23.00)
        weekend=float(weekend/8.00)
        return weekend, weekday

    output=days.map(lambda x: (x[0], daysParser(x[1]))).sortByKey()
    output=output.map(lambda x: "%s\t%.2f, %.2f" %(x[0],x[1][0], x[1][1]))
    output.saveAsTextFile("task7.out")
    sc.stop()
