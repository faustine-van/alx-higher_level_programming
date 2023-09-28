#!/bin/bash
# takes url and display all HTTP REQUEST METHOD
curl -sI "$1" | grep  'Allow:' |cut -d ' ' -f 2- | tr -d '\n'
