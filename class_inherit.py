#!/usr/bin/python
#Filename:class_inherit.py

class Person:
    def __init__(self,country):
        self.country = country
    def speak(self):
        print 'my country is %s' % self.country

class SchoolMember:
    '''Represents any school member'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        '''tell my details'''
        print 'Name:%s   age:%s' % (self.name, self.age)


class Teacher(SchoolMember):
    '''Represent a teacher'''
    def __init__(self, name, age, salary):
        # python would not call base class's constructor, u have to call it by yourself
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary : %d' % self.salary

class Student(SchoolMember, Person):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        Person.__init__(self, 'china')
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tell(self):
        SchoolMember.tell(self)
        Person.speak(self)
        print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

print # prints a blank line

members = [t, s]
for member in members:
    member.tell() # works for both Teachers and Students
