#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        try:
            print(urllib.request.urlopen(response))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
