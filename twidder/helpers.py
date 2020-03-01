import requests
from constants import TWITTER_API_URL


def get_bearer_token(consumer_key, consumer_secret):
    r = requests.post(
        TWITTER_API_URL + "/oauth2/token",
        auth=(consumer_key, consumer_secret),
        data={"grant_type": "client_credentials"},
    )

    if r.status_code != 200:
        raise Exception(
            f"Failed to get bearer token (HTTP {r.status_code}): {r.text}"
        )

    body = r.json()
    return body["access_token"]
