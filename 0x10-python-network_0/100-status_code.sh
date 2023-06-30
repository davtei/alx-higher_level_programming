#!/bin/bash
# A Bash script that sends a request and displays only status code of response
curl -s -o /dev/null -I -w "%{http_code}" "$1"
