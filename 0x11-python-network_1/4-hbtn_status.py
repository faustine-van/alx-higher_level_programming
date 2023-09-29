#!/usr/bin/python3
# fetches https://alx-intranet.hbtn.io/status use the package requests
import requests

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    content = requests.get(url)
        if content.status_code == 200:
            print(f"Body response:\n"
                  f"\t- type: {type(content.text)}\n"
                  f"\t- content: {content.text}"
                )
        else:
            print("failed")
