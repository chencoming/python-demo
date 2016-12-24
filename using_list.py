#!/usr/bin/python

cublist = ['chelsea','manu','manc','liv']

print 'I have:', len(cublist), ' football cubs'

print 'They are:',
for item in cublist:
    print item,

cublist.append('ans')

print '\nMy list is now', cublist

cublist.sort()
print 'my sorted list is now', cublist

print 'The first item', cublist[0]

del cublist[2]
print 'my list is now', cublist

print 'item 1 to 3 is ', cublist[:]
