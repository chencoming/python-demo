#!/usr/bin/python

zoo = ('wolf','elephant','penguin')

print 'number of animals is', len(zoo)

new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in new zoo is', len(new_zoo)

print 'All animals in new zoo are', new_zoo
print 'Old zoo are ', new_zoo[2]
print 'last animal is ',new_zoo[2][0]


age = 22
name = 'jim'

print '%s is %d years old' % (name, age)
print 'where is %s' % (name,) # name or (name) works 

zoo2 = ('a1','a2','a3')
zoo = zoo.__add__(zoo2)
print 'new zoo ', zoo
print 'new zoo ',zoo.__contains__('wolf')
