#!/usr/bin/env python
# Filename: try_except.py

import sys

try:
    s=raw_input('Enter something --> ')
except EOFError:   #like ctrl-d
    print '\nWhy did you do an EOF on me?'
    sys.exit() # exit the program
except:   #like ctrl-c
    print '\nSome error/exception occurred.'
    

print 'Done with input : %s' % s