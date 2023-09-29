#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    args = sys.argv[1]
    url = urllib.request.Request(args[1])
    with urllib.request.urlopen(url) as res:
        print(dict(res.headers).get("X-Request-Id"))
