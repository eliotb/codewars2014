#!/usr/bin/env python3
"""Solution to Kiwi PyCon 2014 codewars problem 1

Eliot Blennerhassett
"""
l = open('01-cipher').readlines()

# eyeballed the input file, and found the relevant line numbers
keys = [k.split('|')[1:3] for k in l[1:50:2]]

# create a translation dictionary
d = dict([(k[0].strip(), chr(int(k[1], base=16))) for k in keys])

# translate the ciphertext
for s in l[53:61]:
    print(''.join([d.get(c, c) for c in s]), end='')
