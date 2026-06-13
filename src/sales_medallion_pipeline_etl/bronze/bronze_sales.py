from pyspark import pipelines as dp

@dp.table(
    name="bronze_sales",
    comment="Raw taxi trip data"
)
def bronze_sales():
    return spark.read.table("samples.nyctaxi.trips")