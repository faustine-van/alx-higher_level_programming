#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen(
        'https://alx-intranet.hbtn.io/status'
    ) as response:
        html = response.read()
        content = html.decode('utf-8')
        content_bytes = html
        type_content = type(html)
    print(f"Body response:\n"
          f"    - type: {type_content}\n"
          f"    - content: {content_bytes }\n"
          f"    - utf8 content: {content}")
