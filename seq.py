#!/usr/bin/python

# list
list = ['first','second','third','forth','fifth','sixth']
print 'values of list:',
for value in list:
    print value,
print '\nanother way to read list:',
for i in range(0,len(list)-1):
    print list[i],
print '\n indexing :', list[-6]
print list[:-5]

    

# tuple
tuple = ('first','second','third','forth','fifth','sixth')
print '\nvalues of tuple:',
for value in tuple:
    print value,
print '\nanother way to read tuple:',
for i in range(0,len(tuple)-1):
    print tuple[i],

# dict
dict = {'first' : 'a',
        'second' : 'b',
        'third' : 'c',
        'forth' : 'd',
        'fifth' : 'e',
        'sixth' : 'f'
        }
print '\nvalues of dict:'
for key,value in dict.items():
    print key,' == ',value,'\n'

string = 'chencoming'
print string[1:-2]
