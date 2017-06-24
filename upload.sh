#!/bin/sh

## User API Key
KEY='HjTgCO8t3Obz1NYEbmQZN/uXjh0xPOYA'

## The URL to upload to, probably don't change this.
URL=http://imagebin.ca/upload.php

curl \
	-F "key=$KEY" \
	-F "file=@$1" \
	"$URL"
