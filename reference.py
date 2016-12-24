#!/usr/bin/python

list = ['first','second','third','forth','fifth','sixth']
newlist = list

del list[0]

print 'list is ', list
print 'newlist is ', newlist

# make a copy by doing a full slice
mylist = list[:]
del list[0]


print 'list is ', list
print 'mylist is ', mylist



