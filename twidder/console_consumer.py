import json
from kafka import KafkaConsumer
from pprint import pprint
from constants import SAMPLED_STREAM_TOPIC

consumer = KafkaConsumer(
    SAMPLED_STREAM_TOPIC,
    group_id="console.consumer",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

for msg in consumer:
    pprint(msg.value)
