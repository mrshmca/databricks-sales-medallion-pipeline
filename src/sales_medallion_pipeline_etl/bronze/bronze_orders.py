from pyspark import pipelines as dp
@dp.table(
    name="bronze_orders",
    comment="Raw order data"
)
def bronze_orders():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .load("/Workspace/Users/monakumarimor@gmail.com/.bundle/sales_medallion_pipeline/dev/files/fixtures/data/orders.csv")
    )