#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    d1 = {"email": sys.argv[2]}
    encoded_d1 = urllib.parse.urlencode(d1)
    final_encode = encoded_d1.encode('utf-8')

    with urllib.request.urlopen(url, data=final_encode) as res:
        response = res.read()
        print(response.decode('utf-8'))
