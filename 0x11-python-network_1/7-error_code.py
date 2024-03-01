#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
prints an error code if an error is returned.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
