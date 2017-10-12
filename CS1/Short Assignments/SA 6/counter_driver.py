'''
filename: counter_driver.py
name: shane berthoud
date: october 15th 2014
purpose: to test the counter class
'''

# imports the counter class from the counter.py file
from counter import Counter

myCounter1 = Counter (30, 30, 2)     # creates an instance of the Counter class, making myCounter1 a Counter object.
print myCounter1                      # prints the initial value of the counter.
print myCounter1.get_value()          # tests .get_value() and prints the initial value of the counter.

while myCounter1.initial > 0:         # while the value of the counter is greater than zero, 
    print myCounter1.tick()           # it will decrement the counter, print whether or not it has looped,
    print myCounter1                  # and print the value.

print myCounter1.tick()               # tests to see what happens after the counter goes below zero
print myCounter1                      # prints the final value

myCounter2 = Counter (60, 60, 2)     # creates an instance of the Counter class, making myCounter2 a Counter object.
print myCounter2                      # prints the initial value of the counter.
print myCounter2.get_value()          # tests .get_value() and prints the initial value of the counter.

while myCounter2.initial > 0:         # while the value of the counter is greater than zero, 
    print myCounter2.tick()           # it will decrement the counter, print whether or not it has looped,
    print myCounter2                  # and print the value.

print myCounter2.tick()               # tests to see what happens after the counter goes below zero
print myCounter2                      # prints the final value