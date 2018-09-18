# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:41:55 2018

@author: Sandman
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def __init__(self, name):         
        Person.name = name
    def say(self, stuff):
        return self.name + ' says: It is obvious that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):         
        return 'It is obvious that ' + self.name + ' says: ' + stuff 