'''
filename: timer_driver.py
name: shane berthoud
date: october 15th 2014
purpose: to test the timer class
'''

# imports the Timer class and the Counter class
from timer import *

myTimer = Timer(1, 30, 30)      # creates an instance of the Timer class, making myTimer a Timer object.

print myTimer                   # prints the initial value of the timer
print myTimer.is_zero()         # checks to make sure this function returns false when it is not "00:00:00"
while not myTimer.is_zero():    # while the Timer doesn't read "00:00:00" the timer will decrement until it does.
    myTimer.tick()
    print myTimer               # prints the value of the timer to the console after .tick()

print myTimer.is_zero()         # checks to make sure this function returns true when it IS "00:00:00"
myTimer.tick()                  # decrements the timer past "00:00:00"
print myTimer                   # prints the result
