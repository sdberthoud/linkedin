'''
filename: soldier_ll.py
name: shane berthoud
date: november 3rd 2014
course: cs 1
purpose: create a linked list of soldiers that can be appended to and deleted from
'''

from soldier import Soldier

class Soldier_LL:
    # instantiates the soldier linked list
    def __init__(self):
        self.first_soldier = Soldier(1)                # sets the first soldier as a soldier numbered 1.
        self.first_soldier.next = self.first_soldier   # sets the next and previous soldier as the first soldier if none have been added.
        self.first_soldier.prev = self.first_soldier
    
    def first_aliveSoldier(self):
        '''a method that takes nothing as parameter and returns the first soldier'''
        return self.first_soldier
    
    def insert_after(self, x, n):
        '''a method that can insert soldiers into the linked list at any point in the linked list that takes a soldier to insert after and the number of a new soldier as parameter.'''
        y = Soldier(n)           # makes the new soldier
        z = x.next               # stores the soldier after the soldier that is going to be inserted after.
        y.prev = x               # makes the 4 new connections with the new soldier in order to add it to the linked list.
        y.next = z
        x.next = y
        z.prev = y
        
    def delete(self, x):
        '''a method that deletes a soldier from the list, taking the soldier to be deleted as input.'''
        if x == self.first_soldier:                           # sets self.first_soldier equal to the next soldier in line so the linked list still works.
            self.first_soldier = self.first_soldier.next
        x.prev.next = x.next
        x.next.prev = x.prev
        
    
    def append(self, n):
        '''a method that that adds soldiers onto the end of the linked list.'''
        last_soldier = self.first_soldier.prev
        self.insert_after(last_soldier, n)