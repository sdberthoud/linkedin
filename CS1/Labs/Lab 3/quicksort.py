'''
filename: quicksort.py
name: shane berthoud
date: november 4th 2014
course: cs 1
purpose: to write the sort function and all of the other functions that come with it.'''

from string import lower

def partition(the_list, p, r, compare_func):
    '''the partition function that checks if the values in the list are greater than or less than the last item in the list and puts them to the right or left of it respectively'''
    pivot = the_list[r]       # sets the variables that run the function
    i = p - 1
    j = p
    while j < r:              # makes sure that this does not happen when j = r. if the item at index j is less than the pivot it swaps the position of i and j, if its greater it just increments j.
        if compare_func(the_list[j], pivot):
            i += 1
            swap(the_list, i, j)
        j += 1
    swap(the_list, i+1, r)    # swaps the item at the index i + 1 which is greater than r with r so the left side of the itemthat was at index r is less than it, and the right side is greater.
    return i+1

def swap(the_list, i, j):
    '''a function to swap the items at indices i and j'''
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp
    
# three functions that compare the values of given instance variables.
def compare_population(city1, city2):
    return city1.pop > city2.pop

def compare_name(city1, city2):
    return lower(city1.name) <= lower(city2.name)

def compare_latitude(city1, city2):
    return city1.lat <= city2.lat

def quicksort(the_list, p, r, compare_func):
    '''function that recursively sorts the list of cities if the length of the list is greater than 1'''
    if p < r:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)
        quicksort(the_list, q+1, r, compare_func)

def sort(the_list, compare_func):
    '''a function that calls quicksort and gives it variables p and r'''
    quicksort(the_list, 0, len(the_list)-1, compare_func)

        