from pyspark import pipelines as dp
from pyspark.sql.functions import sum, count, avg

@dp.table(
    name="gold_sales_metrics",
    comment="Business metrics"
)
def gold_sales_metrics():
    return (
        spark.read.table("silver_sales")
        .groupBy("pickup_zip")
        .agg(
            sum("fare_amount").alias("total_revenue"),
            count("*").alias("trip_count"),
            avg("fare_amount").alias("avg_fare")
        )
    )