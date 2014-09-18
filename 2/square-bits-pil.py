#!/usr/bin/env python2
"""Solution @ to Kiwi PyCon 2014 codewars problem 2

This time, use PIL to draw the QR code as an image
mechanise submit the image to a decoding webservice
lxml to extract the token from the response

Eliot Blennerhassett
"""
# a bit of manual fiddling reveals that there are exactly 21^2 chars
# in the input file. Printing as a square, recognise it as a QR code

from PIL import Image, ImageDraw
import mechanize
import lxml.html

f = open('02-square-bits')
l = f.read()

im = Image.new("RGB", (210, 210), "white")
draw = ImageDraw.Draw(im)

y = 0
for ofs in range(0, len(l), 21):
    s = l[ofs:ofs+21]
    # print(s)   # see it is a QR code
    # Draw QR code image
    x = 0
    for c in s:
        if c == '1':
            draw.rectangle((x, y, x+10, y+10), fill="black")
        x += 10
    y += 10

#im.show()  # See the image is QR code too
im.save('problem3.png', "PNG")

# Submit the image to zxing webservice
br = mechanize.Browser()
response = br.open('http://zxing.org/w/decode.jspx')
br.form = list(br.forms())[1]  # the file upload form
br.form.add_file(open('problem3.png'), 'image/png', 'qr.png')
response = br.submit()
r = response.read()

# Extract the token value
root = lxml.html.fromstring(r)
l = root.xpath('//tr/td//text()')
print 'Token is', l[1]
