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

    reg = requests.get(url)
    if reg.status_code >= 400:
        print("Error code: {}".format(reg.status_code))
    else:
        print(reg.text)
