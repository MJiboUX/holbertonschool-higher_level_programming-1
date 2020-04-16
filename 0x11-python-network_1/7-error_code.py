#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
   displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
        try:
                r = requests.get(sys.argv[1])
                r.raise_for_status()
                print(r.content.decode('utf-8'))
        except requests.exceptions.HTTPError:
                print("Error code: {}".format(r.status_code))
