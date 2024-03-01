#!/usr/bin/env python3
"""
A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        print(f"Your GitHub user id is: {user_id}")
    else:
        print("Error: Failed to retrieve user information")
