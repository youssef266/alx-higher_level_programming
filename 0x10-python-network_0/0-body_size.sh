#!/bin/bash

# Check if URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request and store the response in a variable
response=$(curl -s -w "%{size_download}" -o /dev/null "$1")
