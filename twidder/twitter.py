import requests

TWITTER_API_URL = "https://api.twitter.com"


def handle_http_error(response):
    raise Exception(f"HTTP {response.status_code}: {response.text}")


def get_bearer_token(consumer_key, consumer_secret):
    r = requests.post(
        TWITTER_API_URL + "/oauth2/token",
        auth=(consumer_key, consumer_secret),
        data={"grant_type": "client_credentials"},
    )

    if r.status_code != 200:
        handle_http_error(r)

    body = r.json()
    return body["access_token"]


def stream_sampled_tweets(bearer_token):
    r = requests.get(
        TWITTER_API_URL + "/labs/1/tweets/stream/sample",
        params={"format": "detailed"},
        headers={"Authorization": f"Bearer {bearer_token}"},
        stream=True,
    )

    if r.status_code != 200:
        handle_http_error(r)

    return r.iter_lines()


def get_filtered_stream_rules(bearer_token):
    r = requests.get(
        TWITTER_API_URL + "/labs/1/tweets/stream/filter/rules",
        headers={"Authorization": f"Bearer {bearer_token}"},
    )

    if r.status_code != 200:
        handle_http_error(r)

    return r.json()


def set_filtered_stream_rules(rules, bearer_token):
    r = requests.post(
        TWITTER_API_URL + "/labs/1/tweets/stream/filter/rules",
        headers={"Authorization": f"Bearer {bearer_token}"},
        json={"add": rules},
    )

    if r.status_code != 201:
        handle_http_error(r)

    return r.json()


def stream_filtered_tweets(bearer_token):
    r = requests.get(
        TWITTER_API_URL + "/labs/1/tweets/stream/filter",
        params={"format": "detailed"},
        headers={"Authorization": f"Bearer {bearer_token}"},
        stream=True,
    )

    if r.status_code != 200:
        handle_http_error(r)

    return r.iter_lines()
