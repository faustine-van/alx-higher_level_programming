#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen(
        'https://alx-intranet.hbtn.io/status'
    ) as response:
        html = response.read()
    print("Body response:\n    - type: {}".format(type(html)))
    print("    - content: {}\n    - utf8 content: {}".format(html,
                                                        html.decode('utf-8')))
