#!/bin/bash
# Command to display the size of the content-Length in a header.
curl -sI $1 | grep Content-Length | cut -d" " -f2
