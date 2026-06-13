from pyspark import pipelines as dp
@dp.table(
    name="silver_sales",
    comment="Cleaned sales data"
)
def silver_sales():
    return spark.sql("""

    SELECT
        o.order_id,
        o.customer_id,
        c.customer_name,
        c.city,
        p.product_name,
        p.category,
        CAST(p.price AS DOUBLE) AS price,
        CAST(o.quantity AS INT) AS quantity,
        CAST(p.price AS DOUBLE) * CAST(o.quantity AS INT) AS sales_amount,
        o.order_date

    FROM bronze_orders o
    JOIN bronze_customers c
      ON o.customer_id = c.customer_id

    JOIN bronze_products p
      ON o.product_id = p.product_id

    """)