import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "twitter_sampled_stream",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
)

for msg in consumer:
    print(msg.value)
