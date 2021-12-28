import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.getOrCreate()
od=spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])
od.createOrReplaceTempView("opendata")

output=spark.sql("select precinct, cast(sum(amount_due) as float) as t_amt, cast(avg(amount_due) as float) as a_amt from opendata group by precinct order by precinct asc")
output.select(format_string("%d\t%.2f, %.2f", output.precinct, output.t_amt, output.a_amt)).write.save("task3-sql.out", format = "text")
