#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    html = response.read()
    content = html.decode('utf-8')
    content_bytes = html
    type_content = type(html)
print(f"Body response:\n"
      f"\t- type: {type_content}\n"
      f"\t- content: {content_bytes }\n"
      f"\t- utf8 content: {content}")
