#!/usr/bin/env python2

import slate
import sys

fb = ('one two three four five six seven eight nine ten ' +
'eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen '  +
'twenty twenty-one twenty-two twenty-three twenty-four twenty-five twenty-six twenty-seven')

lfn = fb.split()

txt = ''
for fx in lfn:
    fn = 'page-%s.pdf' % fx
    with open(fn) as f:
        t = slate.PDF(f)
    txt += t[0][0:-1]

with open(sys.argv[1], 'w') as f:
    f.write(txt)

# python 03-pages.py  > pages.txt
# base64 -d pages.txt > pages.png
# view the png "We like the moon" Joel and Alex Veitch rathergood.com
# Hmmm
# exiftool pages.png  -> shows some text in the comment
