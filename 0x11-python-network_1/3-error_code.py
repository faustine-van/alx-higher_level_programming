#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-7).
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            if res.status_code >= 400:
                print(f"Error code: {res.status_code}")
            print(res.decode())
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
