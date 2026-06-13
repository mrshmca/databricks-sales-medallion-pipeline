from pyspark import pipelines as dp
@dp.table(
    name="bronze_products",
    comment="Raw product data"
)
def bronze_products():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .load("/Workspace/Users/monakumarimor@gmail.com/.bundle/sales_medallion_pipeline/dev/files/fixtures/data/products.csv")
    )