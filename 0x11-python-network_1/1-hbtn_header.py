import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    headers = {'X-Request-Id': 'X-Request-Id'}

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        value = response.headers.get('X-Request-Id')
        dispay_page = response.read()
    print(value)
