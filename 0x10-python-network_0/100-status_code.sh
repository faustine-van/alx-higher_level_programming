#!/bin/bash
# get status code using curl
curl -s -o -I -w "%{http_code}" $1
