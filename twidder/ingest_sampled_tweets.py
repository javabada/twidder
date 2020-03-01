import os

from kafka import KafkaProducer

from topics import SAMPLED_STREAM
from twitter import get_bearer_token, stream_sampled_tweets

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")

bearer_token = get_bearer_token(consumer_key, consumer_secret)

producer = KafkaProducer()

lines = stream_sampled_tweets(bearer_token)

for line in lines:
    # filter out keep-alive new lines
    if line:
        producer.send(SAMPLED_STREAM, value=line)
