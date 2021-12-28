import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()
parking = spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])
parking.createOrReplaceTempView("park")

output=spark.sql("select vehicle_make, count(*) AS num FROM park GROUP BY vehicle_make order by num desc limit 1")
output.select(format_string('%s\t%d', output.vehicle_make, output.num)).write.save("task5-sql.out", format="text")
