'''
filename: arithmetic_series.py
name: shane berthoud
date: september 29th 2014
course: CS 1
purpose: short assignment 5, to check if adding a series of numbers is the same as putting the number through the arithmetic series formula.
'''

n = 0

def arithmetic_series(n):
    '''compares the sum of numbers from 0 to n, and the variable n being put in the arithmetic series formula
    parameter: n, which is a number input by the user
    returns: it either returns that the number checks out and the direct method equals the formula, or is returns that there was a problem and one does not equal the other.
    '''
    n = int(raw_input("Enter a number: "))
    
    #a variable that stores the sum of the direct method
    direct = 0
    
    #for-loop that iterates through each number in range 0 to n-1 and adds each number to direct
    for num in range(0, n+1):
        direct = direct + num
    
    #variable that stores the result of substituting user's 'n' into the arithmetic series formula
    series = (n*(n+1))/2
    
    #if statement that checks to see if direct = series
    if direct == series and n > 0:
        return "%d checks out OK." % (n)
    else:
        exit()
        
print arithmetic_series(n)
print arithmetic_series(n)
print arithmetic_series(n)
print arithmetic_series(n)
print arithmetic_series(n)
    
