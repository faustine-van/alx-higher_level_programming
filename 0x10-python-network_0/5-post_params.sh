#!/bin/bash
# take URL send POST display
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
