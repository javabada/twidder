# Twidder

To spin up Kafka:

```shell
docker-compose up
```

To run something that does something:

```shell
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5 --master "local[2]" lang_count.py
```
