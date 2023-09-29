#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys
args = sys.argv[1]
with urllib.request.urlopen(args[1]) as res:
   pass

if 'X-Request-Id' in res.headers:
    print(res.headers['X-Request-Id'])
