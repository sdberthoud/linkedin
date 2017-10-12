'''
filename: where_to_stand.py
name: shane berthoud
date: november 3rd 2014
course: cs 1
purpose: tests all the classes and shows where to stand in all three instances.
'''

from army import *

n = int(raw_input("Enter the number of soldiers, at least 2: "))                                        # saves n and k as input and passes them into the Army class and the last_alive method
k = int(raw_input("Enter the spacing between victims, between 1 and the last number entered: "))
josephus_and_friends = Army(n)
josephus_and_friends.last_alive(k)