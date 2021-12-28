import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()
park = spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])
park.createOrReplaceTempView("park")

output = spark.sql("select vehicle_make, count(*) AS num from park group by vehicle_make order by num desc, vehicle_make asc limit 10") 
output.select(format_string('%s\t%d', output.vehicle_make, output.num)).write.save("task6-sql.out", format = "text")
