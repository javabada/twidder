from configparser import ConfigParser
import json
import pprint
import requests

TWITTER_URL = "https://api.twitter.com"

config = ConfigParser()
config.read("config.ini")

consumer_key = config["twitter"]["consumer_key"]
consumer_secret = config["twitter"]["consumer_secret"]


def get_bearer_token(consumer_key, consumer_secret):
    r = requests.post(
        TWITTER_URL + "/oauth2/token",
        auth=(consumer_key, consumer_secret),
        data={"grant_type": "client_credentials"},
    )
    body = r.json()
    return body["access_token"]


bearer_token = get_bearer_token(consumer_key, consumer_secret)


def connect_stream(token):
    r = requests.get(
        TWITTER_URL + "/labs/1/tweets/stream/sample",
        headers={"Authorization": f"Bearer {token}"},
        stream=True,
    )
    for line in r.iter_lines():
        if line:
            data = json.loads(line)
            pprint.pprint(data)


connect_stream(bearer_token)
