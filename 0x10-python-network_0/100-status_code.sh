#!/bin/bash
curl -s -o -I -w "%{http_code}" $1
