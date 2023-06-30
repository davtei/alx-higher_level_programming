#!/bin/bash
# A Bash script that sends a POST request, displays the body of the response
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
