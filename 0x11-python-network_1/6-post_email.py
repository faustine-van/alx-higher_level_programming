#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":

    url = sys.argv
    d1 = {"email": args[2]}
    res = requests.post(args[1], data=d1)
    content = res.headers.get("email")
    print(content.text)
