#!/usr/bin/env python3
#!/usr/bin/env python3
"""Solution to Kiwi PyCon 2014 codewars problem 2

Eliot Blennerhassett
"""
# a bit of manual fiddling reveals that there are exactly 21^2 chars
# in the input file. Printing as a square, recognise it as a QR code

f = open('02-square-bits')
l = f.read()

from tkinter import *
master = Tk()

canvas_width = 210
canvas_height = 210
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

y = 0
for ofs in range(0, len(l), 21):
    s = l[ofs:ofs+21]
    # print(s)   # see it is a QR code
    # Draw QR code image
    x = 0
    for c in s:
        if c == '1':
            w.create_rectangle(x, y, x+10, y+10, fill="#000000")
        x += 10
    y += 10

mainloop()

# Capture image displayed, submit to online decoder
# http://zxing.org/w/decode.jspx
# Get the secret string
