#!/usr/bin/env python
# Filename: using_file.py

poem = '''\n all of above is bullshit '''
f = file('poem.txt','a') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

# if no mode is specified, 'r'ead mode is assumed by default
f = file('poem.txt') 

while True:
    line = f.readline()
    if len(line)==0: # Zero length indicates EOF
        break
    print line,        # Notice comma to avoid automatic newline added by Python

f.close() # close the file 
