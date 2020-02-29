import json
from configparser import ConfigParser
from kafka import KafkaConsumer
from pprint import pprint

config = ConfigParser()
config.read("config.ini")

topic = config["kafka"]["topic"]

consumer = KafkaConsumer(
    topic,
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
)

for msg in consumer:
    pprint(msg.value)
