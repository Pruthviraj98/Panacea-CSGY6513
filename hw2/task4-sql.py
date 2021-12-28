import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.getOrCreate()
parking=spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])
parking.createOrReplaceTempView("park")

result = spark.sql("select registration_state, count(registration_state) as numstates from (select case when park.registration_state like 'NY' then 'NY' else 'Other' end as registration_state from park) group by registration_state order by registration_state asc")
result.select(format_string('%s\t%d', result.registration_state, result.numstates)).write.save("task4-sql.out", format = "text")
