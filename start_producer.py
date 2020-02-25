import requests
from configparser import ConfigParser
from kafka import KafkaProducer

TWITTER_API_URL = "https://api.twitter.com"

config = ConfigParser()
config.read("config.ini")

consumer_key = config["twitter"]["consumer_key"]
consumer_secret = config["twitter"]["consumer_secret"]


def get_bearer_token(consumer_key, consumer_secret):
    r = requests.post(
        TWITTER_API_URL + "/oauth2/token",
        auth=(consumer_key, consumer_secret),
        data={"grant_type": "client_credentials"},
    )
    body = r.json()
    return body["access_token"]


bearer_token = get_bearer_token(consumer_key, consumer_secret)


def connect_stream(bearer_token):
    r = requests.get(
        TWITTER_API_URL + "/labs/1/tweets/stream/sample",
        params={"format": "detailed"},
        headers={"Authorization": f"Bearer {bearer_token}"},
        stream=True,
    )
    return r.iter_lines()


producer = KafkaProducer()

lines = connect_stream(bearer_token)

for line in lines:
    # filter out keep-alive new lines
    if line:
        producer.send("twitter_sampled_stream", value=line)
