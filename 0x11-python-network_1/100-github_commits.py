#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
    Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


if __name__ == "__main__":
    repos_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repos_name}/commits"
    response = requests.get(url)
    res = response.json()

    for i in range(10):
        sha = res[i].get('sha')
        author = res[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
