#!/usr/bin/python
#Filename:objvar.py

class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self,name):
        '''initializes the person's data.'''
        self.name = name
        print 'Initializing %s' % self.name

        Person.population += 1

    def __del__(self):
        '''i am dying.'''
        print '%s says bye.' % self.name

        Person.population -= 1

        if Person.population == 0:
            print 'Im the last one.'
        else:
            print 'There are still %d people left' % Person.population

    def sayHi(self):
        print 'Hi my name is %s' % self.name

    def howmany(self):
        if Person.population == 1:
            print 'only one'
        else:
            print 'we got %d person here' % Person.population

sp = Person('Swaroop')
sp.sayHi()
sp.howmany()

km = Person('Abdul Kalam')
km.sayHi()
km.howmany()

sp.sayHi()
sp.howmany()
