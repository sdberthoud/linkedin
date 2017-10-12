'''
filename: soldier.py
name: shane berthoud
date: november 3rd 2014
course: cs 1
purpose: create a soldier class that are nodes in the linked list
'''

class Soldier:
    # instantiates a node in the linked list and sets its value as n
    def __init__(self, n):
        self.n = n
        self.next = None
        self.prev = None
        
    def kill(self):
        ''' prints a message displaying that the soldier has been killed, takes no parameters, and returns nothing. '''
        print "Soldier " + str(self.n) + " has been killed."