#!/bin/bash
# OK, lets undo this nested nightmare of formats
uudecode 03-mooooon
file mmmmm-tasty-tasty-data

mv mmmmm-tasty-tasty-data data.xxd.gz
gunzip -f data.xxd.gz

head -n4 data.xxd
# Make my unhexdump.py redundant, thanks Team Cats
# whoda thunk this would exist?
xxd -r data.xxd > data.zip

file data.zip
unzip -q -o data.zip
# get pages/*.pdf

cd pages
rm -f pages.txt
for f in one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one twenty-two twenty-three twenty-four twenty-five twenty-six twenty-seven
do
    pdftotext -nopgbrk "page-$f.pdf"
    cat "page-$f.txt" >> pages.txt
done
cd ..

base64 -d pages/pages.txt > pages.png
file pages.png
exiftool pages.png
echo "See the comment text, work out the secret code"
strings pages.png | tail -n16
