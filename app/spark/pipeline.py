from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql import functions as f

spark = SparkSession \
    .builder \
    .appName("reading boba__order") \
    .config("spark.jars", "/flask_api/postgresql-42.6.0.jar") \
    .getOrCreate()

properties = {
    "user": "db_3d_bubble_tea_db_user",
    "password": "jQ867pZ4a8mXflWofgR7C0PV7swv60rG",
    "driver": "org.postgresql.Driver"
}

url = "jdbc:postgresql://dpg-cj0lihs07spl5oq8ghh0-a.oregon-postgres.render.com:5432/db_3d_bubble_tea_db"
table_name = "boba__order"

# ******

def filtered_df():
    df = spark.read.jdbc(url, table_name, properties=properties)
    # df.show()
    filtered_df = df.filter(df["base"] == "Signature")
    filtered_df.show()
    panda_filtered_df = filtered_df.toPandas()
    # print(panda_filtered_df)

    return panda_filtered_df

def max_base_df():
    df = spark.read.jdbc(url, table_name, properties=properties)
    grouped = df.groupBy('base').count()
    max_base_count = grouped.select(f.max(f.col('count')).alias('count')).collect()[0]['count']
    max_base_df = grouped.filter(f.col('count') == max_base_count).orderBy(f.col('base').desc()).limit(1)
    max_base_panda = max_base_df.toPandas()

    return max_base_panda

def get_max(column_name):
    df = spark.read.jdbc(url, table_name, properties=properties)
    grouped = df.groupBy(column_name).count()

    max_count = grouped.select(f.max(f.col('count')).alias('count')).collect()[0]['count']
    max_df = grouped.filter(f.col('count') == max_count).orderBy(f.col(column_name).desc()).limit(1)
    max_df.show()

    max_panda = max_df.toPandas()
    return max_panda

# print('filtered_df.count :', filtered_df.count())
# print('filtered_df.col ct :', len(filtered_df.columns))
# print('filtered_df.columns:', filtered_df.columns)
# df.describe().show()
# print('df schema 1:')
# filtered_df.printSchema()