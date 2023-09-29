#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.:wq
"""
import urllib.request
import sys


if __name__ == "__main__":

    url = sys.argv[1]

    with urllib.request.urlopen(url) as res1:
        # res1 = res.info()
        print(res1.headers.get("X-Request-Id"))
