#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch me
curl -sL 0.0.0.0:5000/catch_me -X "user_id=98" PUT -H "Origin: HolbertonSchool"
