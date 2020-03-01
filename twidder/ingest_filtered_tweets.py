import os

from kafka import KafkaProducer

from topics import FILTERED_STREAM
from twitter import get_bearer_token
from twitter import get_filtered_stream_rules
from twitter import set_filtered_stream_rules
from twitter import stream_filtered_tweets

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")

bearer_token = get_bearer_token(consumer_key, consumer_secret)

# rules = get_filtered_stream_rules(bearer_token)

# rules = [{"value": "coronavirus OR #coronavirus", "tag": "coronavirus"}]
rules = [{"value": "ozbargain", "tag": "ozbargain"}]

# test = set_filtered_stream_rules(rules, bearer_token)

producer = KafkaProducer()

lines = stream_filtered_tweets(bearer_token)

for line in lines:
    # filter out keep-alive new lines
    if line:
        producer.send(FILTERED_STREAM, value=line)
