import os
import requests
from kafka import KafkaProducer
from constants import TWITTER_API_URL, SAMPLED_STREAM_TOPIC
from helpers import get_bearer_token

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")

bearer_token = get_bearer_token(consumer_key, consumer_secret)

producer = KafkaProducer()

r = requests.get(
    TWITTER_API_URL + "/labs/1/tweets/stream/sample",
    params={"format": "detailed"},
    headers={"Authorization": f"Bearer {bearer_token}"},
    stream=True,
)

for line in r.iter_lines():
    # filter out keep-alive new lines
    if line:
        producer.send(SAMPLED_STREAM_TOPIC, value=line)
