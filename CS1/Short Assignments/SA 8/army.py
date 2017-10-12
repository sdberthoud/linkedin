'''
filename: army.py
name: shane berthoud
date: november 3rd 2014
course: cs 1
purpose: create an army class that makes a linked lists of soldiers and makes it possible to find where to stand in the circle
'''

from soldier import Soldier
from soldier_ll import Soldier_LL

class Army:
    # initializes the army class making the linked list and adding to it the number of soldiers that are passed through as n.
    def __init__(self, n):
        self.circle = Soldier_LL()
        self.number_alive = n                          # sets the number of soldiers alive at first equal to the number of soldiers in the linked lists
        self.victim = self.circle.first_soldier        # sets the victim equal to the first soldier, does not kill him though, phew.
        for i in range( n ):                           # skips 1 when appending soldiers since the first soldier is already set to 1
            if i > 0:
                self.circle.append( i + 1 )
    
    def advance(self, k):
        '''advances the victim k times which it takes as input'''
        for i in range(k):
            self.victim = self.victim.next
    
    def kill_victim(self):
        '''a method that kills the victim, prints that they have been, makes the victim the next person in line and then subtracts from the number of people alive.'''
        self.victim.kill()                               # prints that the victim has been killed and what number soldier the victim is.
        temp = self.victim                               # stores the victim to temp in order to kill the victim and not get rid of the variable self.victim
        self.advance(1)                                  # makes the next person the victim, deletes the victim and subtracts one from the number alive
        self.circle.delete(temp)
        self.number_alive -= 1
        
            
    def last_alive(self, k):
        '''the actual method that will tell you where to stand in the circle in order to not die, takes k which is the number to advance by as parameter.'''
        while self.circle.first_soldier.next != self.circle.first_soldier:                      # checks to see if the first soldier is also the last soldier
            self.advance(k - 1)                                                                 # because you already advance 1 in the kill_victim method you only need to advance by one less than k
            self.kill_victim()                                                                  # kills the next victim
        print "The last remaining soldier is soldier " + str(self.circle.first_soldier.n)       # when the first soldier is the last soldier, the last remaining soldier is printed to the console.