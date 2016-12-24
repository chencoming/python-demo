#!/usr/bin/python
#Filename:class_init.py

class Person:
    '''what is this '''
    def __init__(self, name):
        '''this is a init method of person class'''
        self.name = name
        self.__privateMethod()
    def sayhi(self):
        print 'hello,my name is', self.name
        
    def __privateMethod(self):
        print 'private method only called in class or object\'s body'


p = Person('ming')
print p.__doc__
print p.__init__.__doc__
print Person.__doc__
#print p.__privateMethod()
#print Person.__privateMethod()
#p.sayhi()
