import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.getOrCreate()
opendata=spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])
opendata.createOrReplaceTempView("opendata")

output=spark.sql("select violation, count(*) as counter_violation from opendata group by violation order by violation asc")
output.select(format_string('%s\t%d', output.violation, output.counter_violation)).write.save("task2-sql.out", format = "text")
