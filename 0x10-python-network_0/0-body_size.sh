#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: ./0-body_size.sh <URL>"
  exit 1
fi

# Send the request and store the response in a variable
response=$(curl -sI "$1")

# Extract the Content-Length header from the response
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Check if the Content-Length header is present
if [ -z "$content_length" ]; then
  echo "Content-Length header not found"
  exit 1
fi

# Send a separate request to get the actual response body and measure its size
body_size=$(curl -s "$1" | wc -c)

echo "$body_size"
