#!/bin/bash
# A Bash script that sends a JSON POST request to a URL passed as first arg.
curl -s -H "content-type:application/json" -d @"$2" -X POST "$1"
