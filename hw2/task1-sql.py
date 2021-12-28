import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()
park = spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[1])
opendata = spark.read.format('csv').options(header = 'true', inferschema = 'true').load(sys.argv[2])
park.createOrReplaceTempView("park")
opendata.createOrReplaceTempView("opendata")

output = spark.sql("select park.summons_number, park.violation_county, park.registration_state, park.violation_code, park.issue_date from park left join opendata on park.summons_number = opendata.summons_number WHERE opendata.summons_number is NULL order by park.summons_number asc")
output.select(format_string('%d\t%s, %s, %d, %s', output.summons_number, output.violation_county, output.registration_state, output.violation_code, date_format(output.issue_date,'yyyy-MM-dd'))).write.save("task1-sql.out", format="text")
