#!/bin/bash
# takes in a URL, sends a request to that URL, and displays size of the body of response
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
