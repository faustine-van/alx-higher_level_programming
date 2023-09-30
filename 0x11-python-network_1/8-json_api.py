#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys
import json


if __name__ == "__main__":
    letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}
    if len(sys.argv) >= 2:
        res = requests.post(url, data=data)
        try:
            json_data = res.json
            if len(json_data) == 0:
                print("No result")
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        except ValueError:
            print("Not a valid JSON")
