#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        print("No result")
    else:
        r = requests.post(url, data={'q': sys.argv[1]})
        if len(r.json()) == 0:
            print("No result")
        else:
            d = r.json()
            print("[{}] {}".format(d['id'], d['name']))
