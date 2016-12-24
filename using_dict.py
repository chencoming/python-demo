#!/usr/bin/python

ab = {'jim' : 'jim@qq.com',
      'john' : 'john@11.com',
      'gavin' : 'gavin@12.com'
    }

print 'jim\'s email is %s' % ab['jim']

#add
ab['marry'] = 'marry@ad.com'

#delete
del ab['john']

for name, email in ab.items():
    print '%s\'s email is %s' % (name ,email)

if 'jim' in ab: # ab.has_key('jim')
    print 'jim\'s email is %s' % ab['jim']
