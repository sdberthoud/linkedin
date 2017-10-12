# binary_search.py
# Code provided for CS 1 Short Assignment 7.
# Performs binary search on a sorted list of random numbers.

from random import randint

# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.
def binary_search(the_list, key, left = None, right = None):
    # If using the default parameters, then search the entire list.
    if left == None and right == None:
        left = 0
        right = len(the_list) - 1
    
    # YOU FILL IN THE REST OF THIS FUNCTION.
    # computes the midpoint as the middle index, taking the left of the midpoint of the midpoint is a decimal.
    midpoint = (left + right) / 2
    
    # if the value of left exceeds the value of right, or right becomes less than left, the value is not in the list
    if left > right:
        return None
    
    # if the value is at the midpoint, midpoint is returned
    elif the_list[midpoint] == key:
        return midpoint
    
    # checks if the key is less than the value at the_list[midpoint].
    elif the_list[midpoint] > key:
        return binary_search(the_list, key, left, midpoint - 1)       # calls binary search on the list starting at whatever left was assigned to, until the value to the left of the midpoint.
    # checks if the key is greater than the value at the_list[midpoint]
    elif the_list[midpoint] < key:
        return binary_search(the_list, key, midpoint + 1, right)      # calls binary search on the list starting at the value to the right of the midpoint, until whatever right has been assigned to.
        
# Driver code for binary search.
n = int(raw_input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1
    
# Binary search wants a sorted list.
the_list = sorted(the_list)
print "The list: " + str(the_list)

while True:
    key = raw_input("What value to search for? ('?' to see the list, 'q' to quit): ")
    
    if key == "?":
        print "The list: " + str(the_list)
    elif key == "q":
        break
    else:
        key = int(key)    
        index = binary_search(the_list, key)
        if index == None:
            print str(key) + " not found"
        else:
            print str(key) + " found at index " + str(index)
    