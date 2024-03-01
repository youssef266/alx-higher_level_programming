#!/usr/bin/env python3
"""A script that:
- takes a repository name and owner name as arguments
- sends a request to the GitHub API to retrieve the latest 10 commits
- displays the commit id and the commit message
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            commit_sha = commit["sha"]
            commit_message = commit["commit"]["message"]
            print(f"Commit: {commit_sha}\nMessage: {commit_message}\n")
    else:
        print(f"Error: {response.status_code}")
