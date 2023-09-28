#!/bin/bash
# takes url and display all HTTP REQUEST METHOD
curl -sI "$1" | grep -o 'OPTIONS.*' | tr -d '\n'
