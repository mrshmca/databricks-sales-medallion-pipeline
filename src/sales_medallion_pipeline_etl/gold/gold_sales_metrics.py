from pyspark import pipelines as dp

@dp.table(name="gold_sales_metrics")
def gold_sales_metrics():

    return spark.sql("""

    SELECT
        city,
        SUM(sales_amount) AS total_revenue,
        COUNT(*) AS total_orders,
        AVG(sales_amount) AS avg_order_value

    FROM silver_sales

    GROUP BY city

    """)