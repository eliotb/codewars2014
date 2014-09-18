#!/bin/bash
# OK, lets undo this nested nightmare of formats
uudecode 03-mooooon
file mmmmm-tasty-tasty-data

mv mmmmm-tasty-tasty-data data.xxd.gz
gunzip -f data.xxd.gz

head data.xxd
./unhexdump.py data.xxd data.zip

file data.zip
unzip -o data.zip
# get pages/*.pdf

cd pages
../extract-page-text.py ../pages.txt
cd ..

base64 -d pages.txt > pages.png
file pages.png
exiftool pages.png
echo "See the comment text, work out the secret code"
