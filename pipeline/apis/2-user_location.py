#!/usr/bin/env python3
"""Print the location of a GitHub user using the GitHub API."""

import math
import sys
import time

import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
        minutes = math.ceil((reset_time - time.time()) / 60)
        print("Reset in {} min".format(minutes))
    else:
        data = response.json()
        print(data.get("location"))
