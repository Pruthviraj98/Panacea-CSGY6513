import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.getOrCreate()
park=spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])
park.createOrReplaceTempView("park")

output = spark.sql("select violation_county, cast(sum(weekend) as float)/8 as weekend_average, cast(sum(weekday) as float)/23 as weekday_average from ((select violation_county, 1 as weekend, 0 as weekday from park where day(park.issue_date) in (5, 6, 12, 13, 19, 20, 26, 27)) union all (select violation_county, 0 as weekend, 1 as weekday from park where day(park.issue_date) not in (5, 6, 12, 13, 19, 20, 26, 27))) group by violation_county order by violation_county asc")
output.select(format_string('%s\t%.2f, %.2f', output.violation_county, output.weekend_average, output.weekday_average)).write.save("task7-sql.out", format="text")
