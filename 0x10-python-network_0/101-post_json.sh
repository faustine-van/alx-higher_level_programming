#!/bin/bash
# post json
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
