#!/usr/bin/env python2
"""Solution to Kiwi PyCon 2014 codewars problem 4

Eliot Blennerhassett
"""
from zipfile import ZipFile

# I really did this by hand: Unzip 04-hansel-gretel.zip
z = ZipFile('04-hansel-and-gretel.zip')

# But this is not so hard...
with z.open('path.txt') as f:
    d = f.read()

x = y = 0
xmax = ymax = xmin = ymin = 0

# First find the extents of the walk
for c in d:
    if c == 'N':
        y -= 1
    elif c == 'S':
        y += 1
    if c == 'W':
        x -= 1
    elif c == 'E':
        x += 1

    xmax = max(x, xmax)
    ymax = max(y, ymax)
    xmin = min(x, xmin)
    ymin = min(y, ymin)

print xmin,ymin, xmax, ymax
# now display it
from Tkinter import Tk, Canvas, mainloop
master = Tk()
w = Canvas(master, width=xmax, height=ymax)
w.pack()

x = y = 0
for c in d:
    if c == 'N':
        y -= 1
    elif c == 'S':
        y += 1
    if c == 'W':
        x -= 1
    elif c == 'E':
        x += 1
    elif c == '*':
        w.create_line(x,y,x+1,y+1)

mainloop()

# Look at Tk canvas and see "The secret code is BRD6P2WQ"
