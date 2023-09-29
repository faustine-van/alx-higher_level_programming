#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
    displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

args = sys.argv
url = args[1]
res = requests.get(url)
print(res.headers['X-Request-Id'])
