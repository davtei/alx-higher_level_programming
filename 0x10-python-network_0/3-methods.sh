#!/bin/bash
# A Bash script that displays all HTTP methods a server will accept.
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
