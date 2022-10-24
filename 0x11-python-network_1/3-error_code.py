#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
(handling HTTP errors)
"""

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys



if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as resp:
            body = resp.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
