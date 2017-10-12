'''
filename: counter.py
name: shane berthoud
date: october 15th 2014
purpose: create a Counter class that counts down to zero from a given initial and limit
'''

# Create the counter class
class Counter:
    # initialize the Counter class
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        self.min_digits = min_digits
        self.counter = 0   # a variable that helps to find if the counter has looped
        
        # if the initial value of the counter is greater than 0 or is equal to zero, then the value of self.initial is the given initial.
        if initial >= 0 and initial <= self.limit - 1:
            self.initial = initial
        # if the value of initial is greater than the given limit - 1 or less than 0, the initial is self.limit - 1
        else:
            self.initial = self.limit - 1
    
    # defines the function get_value which returns the counter's value as an integer.
    def get_value(self):
        return self.initial
    
    # defines the __str__ function which will return the value of the counter as a string.
    def __str__(self):
        new_string = str(self.initial)    #creates a new variable that stores the value of the counter as a string
        
        # loop that checks to  if length of new_string is less than the minimum digits, if it is, it will add a zero to the beginning of new_string.
        while len(new_string) < self.min_digits:
            new_string = "0" + new_string
        return new_string
    
    # defines a function that will decrement the value of counter and return either True or False.
    def tick(self):
        self.initial -= 1    # decrements the value of the counter.
        
        # if the value of the counter is less than zero it will change the value of the counter to the limit -1
        if self.initial < 0:
            self.initial = self.limit - 1
            self.counter += 1    # adds 1 to the variable self.counter if the counter has wrapped around
        
        #will have the function return True if the function has wrapped around and False if it has not.
        if self.counter > 0:
            return True
        else: 
            return False