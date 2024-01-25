#!/bin/bash

# Check if the URL is provided as an argument.
if [[ -z $1 ]]; then
  echo "Usage: bash script.sh <URL>"
  exit 1
fi

# Store URL in a variable.
url=$1

# Send the request and store in a variable.
response=$(curl -sI "$url")

# Extract the content length from the response headers.
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Check if the content length is empty.
if [[ -z $content_length ]]; then
  echo "Unable to determine the size of the response body."
else
  echo "Size of the response body: $content_length bytes"
fi
