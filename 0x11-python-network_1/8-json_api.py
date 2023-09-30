#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}
    if len(sys.argv) == 2:
        data['q'] = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data=data)
    try:
        json_data = res.json
        if json_data:
            print("[{}] {}".format(json_data.text.get('id'), json_data.text.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
