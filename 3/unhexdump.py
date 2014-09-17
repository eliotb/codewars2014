#!/usr/bin/env python3

"""Part of Solution to Kiwi PyCon 2014 codewars problem 2

Converts hexdump data back into original binary file

Eliot Blennerhassett
"""

from sys import argv

f = open(argv[1])
ll = f.readlines()

with open(argv[2], 'wb') as out:
    for l in ll:
        hexdata = l[9:49].split()
        #print(l)
        #print(hexdata)
        for d in hexdata:
            # not sure about the endian
            i = int(d[0:2], base=16)
            j = int(d[2:4], base=16)
            out.write(bytes([i,j]))

# file 03-unhex -> Zip archive data
# mv 03-unhex 03-unhex.zip
# unzip 03-unhex.zip -> directory pages, with 20 pdfs
# Each pdf contains base64 encoded text
# Quick check shows that this is probably png image
# need to extract and concatenate text from pdf
# base64 decode, then display image
