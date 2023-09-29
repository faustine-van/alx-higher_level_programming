#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":

    res = requests.get(argv[1])
    data = {"email": argv[2]}
    print("Your email is:", res.headers.get(res, data))
