#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":

    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: ", res.status_code)
    print(res.text)
