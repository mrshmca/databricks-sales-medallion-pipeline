from pyspark import pipelines as dp
from pyspark.sql.functions import col

@dp.table(
    name="silver_sales",
    comment="Cleaned taxi trips"
)
def silver_sales():
    return (
        spark.read.table("bronze_sales")
        .filter(col("fare_amount") > 0)
        .filter(col("trip_distance") > 0)
        .dropDuplicates()
    )