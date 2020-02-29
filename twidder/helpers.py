import requests
from .constants import TWITTER_API_URL


# TODO: error handling
def get_bearer_token(consumer_key, consumer_secret):
    r = requests.post(
        TWITTER_API_URL + "/oauth2/token",
        auth=(consumer_key, consumer_secret),
        data={"grant_type": "client_credentials"},
    )
    body = r.json()
    return body["access_token"]
