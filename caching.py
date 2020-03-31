import redis
import requests
import json
import datetime

redis = redis.Redis()
GITHUB_URL = "https://api.github.com/users/"


def get_github_profile(username):
    # Read from cache, otherwise fetch
    result = redis.get(username)

    if not result:
        return fetch_github_profile(username)
    else:
        return {
                "cached": True,
                "profile": json.loads(result.decode("utf-8", "strict").replace("'", '"'))
            }



def fetch_github_profile(username):
    # Gets the result from Github and caches it
    result = requests.get(GITHUB_URL + username)

    print(result.json())
    redis.setex(username, 10, json.dumps(result.json()))
    return {
            "cached": False,
            "profile": result.json()
        }
