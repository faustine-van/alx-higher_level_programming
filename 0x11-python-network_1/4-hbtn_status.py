#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status use the package requests
import requests

url = "https://alx-intranet.hbtn.io/status"
content = requests.get(url)

print(f"Body response:\n"
      f"\t- type: {type(content.text)}\n"
      f"\t- content: {content.text}"
      )
