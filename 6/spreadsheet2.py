#!/usr/bin/env python2
"""Second try for second part of Solution to Kiwi PyCon 2014 codewars problem 6

Use python eval to evaluate the formulae.
!Dangerous if the CodeMaster is Evil!

Eliot Blennerhassett
"""

import mechanize
import lxml.html
from math import sqrt
import re


def table_value(table, cellid):
    # Extract value from cellid
    # table cols A-Z, rows 1-100
    col = cellid[0]
    row = cellid[1:]

    index = (int(row) - 1) * 26 + ord(col) - ord('a')
    val = int(l[index])
    #print '%s=%d' % (cellid, val)
    return val

def lookup(match):
    val = table_value(l, match.group())
    return str(val)

# Regex for cell IDs
p = re.compile(r'[a-z]\d+')

br = mechanize.Browser()
response = br.open('https://codewars.nzpug.org/spreadsheet/question-001')

for i in range(1000):
    r = response.read()

    try:
        br.form = list(br.forms())[0]
    except IndexError: # maybe there won't be a form in the last one?
        print r

    formula = br['formula'].lower() # lower so function names match python ones
    print 'Formula', formula,
    if formula.startswith('secret'):
        break

    # Get list of values in spreadsheet
    root = lxml.html.fromstring(r)
    l = root.xpath('//tr/td//text()')

    # Substitute cell references with values
    ff = p.sub(lookup, formula)
    print '=', ff,

    # Eeek, I hope the codemaster is not too evil!
    # Evaluate the formula
    solution = int(eval(ff))
    print '= %d' % solution
    br['solution'] = str(solution)

    response = br.submit()

