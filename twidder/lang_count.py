from configparser import ConfigParser
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StringType

config = ConfigParser()
config.read("config.ini")

topic = config["kafka"]["topic"]

spark = SparkSession.builder.appName("lang_count").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", topic)
    .option("startingOffsets", "earliest")
    .load()
    .selectExpr("CAST(value AS STRING)")
)

schema = StructType().add("data", StructType().add("lang", StringType()))

lang_df = df.select(from_json(df.value, schema).alias("json")).select(
    "json.data.lang"
)

lang_count = lang_df.groupBy("lang").count()

query = lang_count.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()
