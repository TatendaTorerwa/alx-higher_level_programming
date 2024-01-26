#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status.
"""

import requests

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    html = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
