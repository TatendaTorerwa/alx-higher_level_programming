#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    headers = {'X-Request-Id': 'X-Request-Id'}

    res = requests.get(url, headers=headers)
    print(res.text)
