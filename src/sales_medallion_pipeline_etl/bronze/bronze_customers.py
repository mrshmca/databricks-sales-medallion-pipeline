from pyspark import pipelines as dp
@dp.table(name="bronze_customers", comment="Raw customer data")
def bronze_customers():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .load("/Workspace/Users/monakumarimor@gmail.com/.bundle/sales_medallion_pipeline/dev/files/fixtures/data/customers.csv")
    )