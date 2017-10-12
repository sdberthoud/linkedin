'''
filename: counter.py
name: shane berthoud
date: october 15th 2014
purpose: to make a timer class that takes hours. minutes and seconds as input, makes them counters and counts down the time given.
'''

# imports the counter class from the counter.py file
from counter import Counter

# set variables that can be changed to change all instances. 
MIN_DIGITS = 2
LHOURS = 24
LMINUTES = 60
LSECONDS = 60

# Create the Timer class
class Timer:
    # initialize the Timer class, taking hours, minutes and seconds as input.
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(LHOURS, hours, MIN_DIGITS)          # sets self.hours to be a Counter object with limit: 24, initial value: hours, and min_digits: 2
        self.minutes = Counter(LMINUTES, minutes, MIN_DIGITS)    # sets self.minutes to be a Counter object with limit: 60, initial value: minutes, and min_digits: 2
        self.seconds = Counter(LSECONDS, seconds, MIN_DIGITS)    # sets self.seconds to be a Counter object with limit: 60, initial value: seconds, and min_digits: 2
    
    # defines the __str__ function which returns the values of self.hours, self.minutes and self.seconds in the format "00:00:00"
    def __str__(self):
        # because the __str__ function in the counter class adds zeros to the value of the counter, zeros will automatically be added.
        str_hrs = str(self.hours)    # sets str_hrs to be the value of self.hours as a string.
        str_min = str(self.minutes)  # sets str_min to be the value of self.minutes as a string.
        str_sec = str(self.seconds)  # sets str_sec to be the value of self.seconds as a string.
        return str_hrs + ":" + str_min + ":" + str_sec
    
    #defines the function that decrements seconds and makes the Timer class act like a timer.
    def tick(self):
        self.seconds.initial -= 1     # decrements the value of seconds
        # checks to see if the value of seconds is less than zero, if it is the value of seconds will become 59 and will decrement minutes.
        if self.seconds.initial < 0:
            self.seconds.initial = self.seconds.limit - 1
            self.minutes.initial -= 1 # decrements the value of minutes
        # checks to see if the value of minutes is less than zero, if it is the value of minutes will become 59 and will decrement hours.
        if self.minutes.initial < 0:
            self.minutes.initial = self.minutes.limit - 1
            self.hours.initial -= 1 # decrements the value of hours
        # checks to see if the value of hours is less than zero, if it is the value of hours will become 23
        if self.hours.initial < 0:
            self.hours.initial = self.hours.limit - 1
    
    # function that will return True if the Timer reads "00:00:00"
    def is_zero(self):
        if self.hours.initial == 0 and self.minutes.initial == 0 and self.seconds.initial == 0:
            return True
        return False