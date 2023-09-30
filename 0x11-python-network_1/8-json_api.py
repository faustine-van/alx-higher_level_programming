#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = {"q": ""}

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}
    res = requests.post(url, data=data)
    try:
        json_data = res.json
        if not json_data:
            print("No result")
        else:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
