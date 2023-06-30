#!/bin/bash
# A Bash script that takes in a URL, sends a GET request and displays response
curl -sfL "$1" -X GET
