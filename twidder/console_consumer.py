import json
from pprint import pprint

from kafka import KafkaConsumer

from topics import FILTERED_STREAM

consumer = KafkaConsumer(
    FILTERED_STREAM,
    group_id="console.consumer",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

for msg in consumer:
    pprint(msg.value)
