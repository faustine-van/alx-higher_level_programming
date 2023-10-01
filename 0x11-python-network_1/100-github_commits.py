#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
    Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    res = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                  res[i].get('sha'),
                  res[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
