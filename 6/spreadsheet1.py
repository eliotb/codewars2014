#!/usr/bin/env python2
"""First try for second part of Solution to Kiwi PyCon 2014 codewars problem 6

'Manually' parse the formulae and evaluate them.

Eliot Blennerhassett
"""

import mechanize
import lxml.html
from math import sqrt

br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
#br.set_handle_robots(False)   # ignore robots
#br.set_handle_refresh(False)  # can sometimes hang without this
# br.addheaders =   	      	# [('User-agent', 'Firefox')]

def table_value(table, cellid):
# table cols A-Z, rows 1-100
# index = (row - 1) * 26 + ord(col) - ord('A')
    col = cellid[0]
    row = cellid[1:]

    index = (int(row) - 1) * 26 + ord(col) - ord('a')
    val = int(l[index])
    #print '%s=%d' % (cellid, val)
    return val

funcs = {'sqrt' : sqrt, 'max': max }

url = 'https://codewars.nzpug.org/spreadsheet/question-001'
response = br.open(url)

for i in range(100):
    r = response.read()      # the text of the page
    #print r

    try:
        br.form = list(br.forms())[0]
        #print br.form
    except IndexError:
        print r

    root = lxml.html.fromstring(r)
    l = root.xpath('//tr/td//text()')
    #print '%d values' % len(l)

    formula = br['formula'].lower()

    print 'Formula', formula
    try:
        parens = formula.index('(')
        try:
            fp = formula.strip(')').split('(')
            #print 'Formula parts', fp
            operands = fp[1].split(',')
            #print 'Operands', operands
            values = [table_value(l, o.strip()) for o in operands]
            print operands
            fn = fp[0]
            #print 'Apply %s to %s' % (fn, values)
            solution = funcs[fn](*values)
            solution = int(solution)
        except Exception, e:
            print e
    except ValueError:
        # print 'No parens'
        fp = formula.split()
        print 'Formula parts', fp
        operand1 = fp[0]
        solution = table_value(l, operand1)

        for i in range(1, 10, 2):
            try:
                operator = fp[i]
                operand2 = fp[i + 1]
            except:
                break

            val2 = table_value(l, operand2)

            # print operand1,val1, operator, operand2, val2

            if operator == '+':
                solution = solution + val2
            elif operator == '-':
                solution = solution - val2
            elif operator == '*':
                solution = solution * val2
            elif operator == '/':
                solution = solution / val2
            else:
                raise ValueError('Unsupported operator <%s> in %s' % (operator, formula))


    print 'Answer = %d' % solution
    br['solution'] = str(solution)

    response = br.submit()

