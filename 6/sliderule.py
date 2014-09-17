#!/usr/bin/env python2
"""First part of Solution to Kiwi PyCon 2014 codewars problem 6

Look into the images and find the offset of the red bar
Eliot Blennerhassett
"""
from PIL import Image

for i in range(1, 16):
    fn = 'secret-line-%02d.png' % i
    im = Image.open(fn)
    id = list(im.getdata())
    try:
        zp = id.index(0) # find the offset of the red line
    except:
        zp = 0
    print i, zp, 120 - zp # last figure is reverse offset

# Update the reverse offsets in html file,
# Now see: https://codewars.nzpug.org/spreadsheet/
