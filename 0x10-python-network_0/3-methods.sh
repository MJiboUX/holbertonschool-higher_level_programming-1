#!/bin/bash
# This Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sI -X ALLOW $1 | sed -n 's/^Allow: //p'
