#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password) and
  uses the GitHub API to display your id
- You must use Basic Authentication with a personal access token as
  password to access to your information (only read:user permission is needed)
- The first argument will be your username
- The second argument will be your password
(in your case, a personal access token as password)
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    my_user_name = sys.argv[1]
    my_pass = sys.argv[2]
    url = "https://api.github.com/users/" + my_user_name

    res = requests.get(url, auth=HTTPBasicAuth(my_user_name, my_pass))
    res1 = res.json()
    print(res1.get('id'))
# print(final_one.get('id'))
