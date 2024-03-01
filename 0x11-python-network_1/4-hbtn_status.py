#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses requests package
this is for getting requests
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
content = response.text

print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
