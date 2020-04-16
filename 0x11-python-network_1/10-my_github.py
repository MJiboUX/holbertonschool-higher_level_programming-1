#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
   and usesthe Github API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    token = '1a0e182fb314d4c9fd8257b7b1a4e345874da1fa'
    url = 'https://api.github.com/user'
    try:
        r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
        print(r.json()['id'])
    except KeyError:
        print("None")
